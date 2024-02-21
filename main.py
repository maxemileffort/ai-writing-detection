import streamlit as st
import pandas as pd
import docx
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Fetch the API key from the .env file
client = OpenAI()
# openai.api_key = os.getenv('OPENAI_API_KEY')

# Custom CSS for the text box
st.markdown("""
    <style>
    textarea {
        font-family: Arial, Helvetica, sans-serif; 
        font-size: 16px; 
        border-radius: 8px; 
        border: 1px solid #ced4da;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Text input for the prompt (First Stage)
prompt = st.text_area('Enter the prompt here:', height=300)
corpus_size = st.slider('Select Corpus Size', 1, 10, 2, 1)
ai_match_percentage = st.slider('AI Match Percentage Threshold', 1, 100, 75)

# Function to read file contents
def read_file(uploaded_file):
    if uploaded_file.name.endswith('.txt'):
        return uploaded_file.read().decode('utf-8')
    elif uploaded_file.name.endswith(('.doc', '.docx')):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

def generate_corpus(prompt, num_variations=5):
    corpus = []
    for _ in range(num_variations):
        response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"write an essay that answers this prompt: {prompt}"}
        ]
    )
        corpus.append(response.choices[0].message.content.strip())
    return corpus

# Function to compare texts with ChatGPT
def compare_texts_with_chatgpt(student_text, corpus):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Compare the following two texts on a scale of 1-100 based on vocabulary, " +
                                        f"sentence patterns, ideas, organization, and tone. \nText 1:\n {student_text} "+
                                        f" \nText 2: \n{corpus} \nResponse Format: \nVocabulary: [score]\n " + 
                                        f"sentence patterns: [score]\n ideas: [score]\n organization: [score]\n tone: [score], " +
                                        f"where [score] is the score of the student text."}
        ]
    )
    score = response.choices[0].message.content.strip()
    return score

# Button to generate corpus
if st.button('Generate Corpus'):
    corpus = generate_corpus(prompt, corpus_size)
    st.session_state['corpus'] = corpus  # Save corpus in session state
else:
    corpus = st.session_state.get('corpus', [])

# File uploader (Second Stage)
uploaded_files = st.file_uploader("Upload student papers (.docx, .doc, .txt files):", accept_multiple_files=True)
st.info('For Google Docs, please download them as .docx files before uploading.')

uploaded_texts = []
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_text = read_file(uploaded_file)
        uploaded_texts.append((uploaded_file.name, file_text))

# Button to analyze papers
if st.button('Analyze Papers'):
    analysis_results = []
    for file_name, paper_text in uploaded_texts:
        score = compare_texts_with_chatgpt(paper_text, "\n\n".join(corpus))
        analysis_results.append((file_name, score))
    st.session_state['analysis_results'] = analysis_results  # Save results in session state

# Displaying the analysis results (Third Stage)
if 'analysis_results' in st.session_state:
    results_df = pd.DataFrame(st.session_state['analysis_results'], columns=['File Name', 'AI Probability'])
    st.write('AI Detection Results')
    st.dataframe(results_df)
    for file_name, _ in st.session_state['analysis_results']:
        st.button(file_name, on_click=lambda: show_detailed_analysis(file_name, file_text))

# # Analyze each paper and store the results
# analysis_results = []
# for file_name, paper_text in uploaded_texts:
#     score = compare_texts_with_chatgpt(paper_text, "\n\n".join(corpus))
#     analysis_results.append((file_name, score))

# # Displaying the analysis results (Third Stage)
# results_df = pd.DataFrame(analysis_results, columns=['File Name', 'AI Probability'])
# st.write('AI Detection Results')
# st.dataframe(results_df)

# Detailed analysis modal
def show_detailed_analysis(file_name, file_text):
    with st.expander(f"Analysis for {file_name}"):
        st.write(file_text)
        # Additional details can be added here



