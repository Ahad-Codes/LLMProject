import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import json
from utils.prompts import task_division_prompt, format_prompt, random_prompt

from langchain_openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class ProjectManagerAgent:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        #self.memory = ConversationBufferMemory()
        #self.image_llm = OpenAI(temperature=0.9)

    def get_response(self, user_idea: str, company_name: str, type_s) -> dict:

        if type_s == "task":
            proo = task_division_prompt(user_idea, company_name)
            print("Generating Tasks from User Prompts...")
            response = self.llm.invoke(proo).content

        structured_response = json.loads(response)

        for agent, task in structured_response.items():
            print(f"Task for {agent}: \n {task} \n")

        return structured_response
