import openai
from tqdm import tqdm
openai.api_key = "YOUR_OPENAI_KEY"

class GptGenerationTopic:

    topicGPT = ""

    def __init__(self, topic):
        self.topicGPT = topic


    def generateMultipleAnswerQuestions(self):
        # code for method1
        content = f"Topic: {self.topicGPT}.\nWrite 5 multiple choice questions with 1 correct answer and 4 incorrect distractor answers each one. Answers should be labelled A to E. Each answer should have an explanation. Please write it in Spanish"
        with tqdm(total=1, desc="Generating multiple choice questions") as pbar:
            response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
										messages = [{"role": "user", "content": content }])
            pbar.update()
        return "n" + response.choices[0].message.content

    def generateSummary(self):
        # code for method2
        content = f"Topic: {self.topicGPT}.\nWhat are 5 key points I should know when studying the topic above?. Please write it in Spanish"
        with tqdm(total=1, desc="Generating summary") as pbar:
            response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
										messages = [{"role": "user", "content": content }])
            pbar.update()
        return "n" +  response.choices[0].message.content

    def generateFlashcards(self):
        # code for method3        
        content = f"Topic: {self.topicGPT}.\nCreate a two-column spreadsheet with questions and corresponding answers on the topic above. Please write it in Spanish.\nQuestion | Answer"
        with tqdm(total=1, desc="Generating Flashcards") as pbar:
            response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
										messages = [{"role": "user", "content": content }])
            pbar.update()
        return "n" +  response.choices[0].message.content

    def generateMindMap(self):
        # code for method4
        content = f"Topic: {self.topicGPT}.\nCreate a mind map on the topic above. List out the central idea, main branches, and sub-branches. Please write it in Spanish"
        with tqdm(total=1, desc="Generating Mindmap") as pbar:
            response = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
										messages = [{"role": "user", "content": content }])
            pbar.update()
        return "n" +  response.choices[0].message.content
