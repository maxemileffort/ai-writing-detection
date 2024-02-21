# AI Writing Detection

## See it live!
[Here.](https://ai-writing-detection-7cvpizdtfonqn2sevysgos.streamlit.app/)

Note: If it doesn't seem to be working, it's likely I have gone over the budget for the month. See below for how to add your own API Key after cloning the repo and creating your own version.

## Writing samples to test:
GDrive with writing assignment and papers to download:
[Drive Link](https://drive.google.com/drive/folders/14o4XU1RlcMnRyVnRxQxq3Wd6-Lfi25Ih?usp=sharing)
The AI paper is the one titled "The Language of Stars: My Journey into Amateur Astronomy". The rest are real papers written by real students.

## Passing OpenAI API Key:
[See here for the steps to do that.](https://discuss.streamlit.io/t/struggling-with-setting-openai-api-using-streamlit-secrets/37959/4)

## How it works
When you land, you can give the tool a prompt in the first box. Next, choose your corpus size. The corpus is a body of text that will be generated based on your prompt.
This tool uses the corpus to evaluate given texts. If there is a high degree of similarity between the corpus and the given paper, then it's likely there was some AI involvement with the paper.

Next, give the tool the papers you wish to assess for AI content. The tool then compares the text in the papers to the text in the corpus. If things like sentence structure and vocab
line up a little too well, then the analysis at the end will tell us that there is a high likelihood of AI being used to generate the content.

You can use the links above to check out the tool. There is a prompt as well as some papers, which have been de-identified. There are also some papers that were explicitly generated with AI, so you can see how the scores stack up.

## A Demo... but in screenshots:
![Step 1. Add prompt](/images/step1.jpg)
1. Add prompt.
2. Choose corpus size.
3. Ignore the next slider, as it's not functional yet. Simply generate the corpus.

![Step 3. Generate corpus](/images/step3.jpg)

4. While the corpus is generating, the next boxes will be greyed out. Go put on some coffee!

![Step 3b. Progress bar... sort of.](/images/step3b.jpg)

5. There is also a "progress bar" on the top right that lets you know it's still working.

![Step 4. Add papers](/images/step4.jpg)

6. When everything lights back up and the progress bar stops, it's time to add some papers. Use the links above for some samples if you don't have any handy.
You can add papers either by dragging and dropping, or simply browsing. Try not to do more than 5, or the API will break because of my spending limit.

![Step 5. Analyze](/images/step5.jpg)

7. Click analyze.

![Step 6. Results](/images/results.jpg)

8. Check the results. I had hoped to be able to click each button below to create a modal for sampling papers with highlights of the AI parts, but that was really beyond the scope of the project, which was just to get to know the API for chatGPT.