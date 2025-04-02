import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import json
from utils.prompts import task_division_prompt, format_prompt, random_prompt

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ProjectManagerAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0.7)
        #self.memory = ConversationBufferMemory()
    
    def get_response(self, user_idea: str, type_s) -> dict:

        if type_s == "task":
            proo = task_division_prompt(user_idea)
            print("Generating Tasks from User Prompts...")
            response = self.llm.invoke(proo).content
        elif type_s == "format":
            response = self.llm.invoke(format_prompt(user_idea)).content
            print(f'FORMAT RESPONSE : \n {response}')
        else:
            response = self.llm.invoke(random_prompt(user_idea)).content

        structured_response = json.loads(response)
        print('Generated Tasks!')

        for agent, task in structured_response.items():
            print(f"Task for {agent}: \n {task} \n")

        return structured_response
    

