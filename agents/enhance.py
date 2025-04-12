import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from utils.prompts import expand_prompt, format_prompt
import json

load_dotenv()
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']


class EnhanceAgent():

  def __init__(self):
    self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)

  def expand(self, agent_type: str, user_idea, short_plan: str):
    char_limit = 100
    prompt = expand_prompt(short_plan, user_idea, agent_type)
    response = self.llm.invoke(prompt).content

    print(f"🔍 Response from {agent_type}: \n\n {short_plan[:char_limit]}")
    print(f"\n 🔍 Expanded for {agent_type}: \n\n {response[:char_limit]} \n")

    return response

  def format(self, agent_type: str, plan: str):

    prompt = format_prompt(plan)
    print(f"Formatting plan for {agent_type}...")
    raw_response = self.llm.invoke(prompt).content
    print(f"Raw response from LLM: {raw_response}")
    response = json.loads(raw_response)
    print(f"Formatted plan for {agent_type}! : {response}")
    return response
