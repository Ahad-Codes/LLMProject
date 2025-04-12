from projectman import ProjectManagerAgent
from agents.marketing import MarketingAgent
from agents.legal import LegalAgent
from agents.coding import CodingAgent
from agents.enhance import EnhanceAgent
from agents.prez import PrezAgent
from utils.image_generator import generate_image

from fastapi import FastAPI
import httpx
from pydantic import BaseModel
from typing import Dict, Any
import asyncio
import os
from dotenv import load_dotenv
import requests
from write_docs import write_docx
import json

load_dotenv()
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
app = FastAPI()

AGENT_ENDPOINTS = {
    "marketing":
    "https://68b9-35-198-236-96.ngrok-free.app/marketing/generate",
    "legal": "https://2d14-34-126-109-14.ngrok-free.app/generate",
    "engineering": "https://68b9-35-198-236-96.ngrok-free.app/project/generate"
}


class TaskRequest(BaseModel):
    tasks: Dict[str, Dict[str, Any]]


@app.post("/tasks")
def process_tasks():

    full_pipeline = True

    #init agents
    pm_agent = ProjectManagerAgent()

    #dummy User Input
    company_name, user_idea = [
        "FoodieFinder",
        "An AI-curated app for discovering local dining experiences and personalized food recommendations."
    ]

    structured_tasks = pm_agent.get_response(user_idea,
                                             company_name,
                                             type_s="task")
    all_responses = {}

    #logo_generation = generate_image(structured_tasks["logo_prompt"])

    if full_pipeline:  #########################

        marketing_agent = MarketingAgent(AGENT_ENDPOINTS["marketing"])
        legal_agent = LegalAgent(AGENT_ENDPOINTS["legal"])
        engineering_agent = CodingAgent(AGENT_ENDPOINTS["engineering"])
        enhance_agent = EnhanceAgent()

        for agent, task_data in structured_tasks.items():

            print(f"Waiting for response from {agent}...")
            try:
                if agent == "logo_prompt":
                    pass

                if agent == "marketing":
                    short_plan_response = marketing_agent.get_response(
                        f"{company_name} - {user_idea}", task_data)

                    response = enhance_agent.expand(
                        agent, f"{company_name} - {user_idea}",
                        short_plan_response)

                elif agent == "legal":
                    short_plan_response = legal_agent.get_response(
                        f"{company_name} - {user_idea}", task_data)

                    response = enhance_agent.expand(
                        agent, f"{company_name} - {user_idea}",
                        short_plan_response)

                elif agent == "engineering":

                    response = engineering_agent.get_response(
                        f"{company_name} - {user_idea}", task_data)

                if response:
                    all_responses[agent] = response

            except Exception as e:
                print(f"Error processing task for {agent}: {e}")

        for agent, response in all_responses.items():
            if agent == "marketing" or agent == "legal":
                print(f'Sending {agent} for Formatting...')
                formatted_response = enhance_agent.format(agent, response)
                print("Back in main")
                all_responses[agent] = formatted_response

    if not all_responses:

        with open(r"outputs/all_responses.json", "r") as file:
            all_responses = json.load(file)
            print("Loaded all responses! \n")

    if all_responses:
        write_docx(all_responses, name=company_name, idea=user_idea)
        print("✅ Responses from Agents completed.")

        #with open("outputs/all_responses.json", "w") as f:
        #json.dump(all_responses, f)

        prez_agent = PrezAgent(all_responses["marketing"],
                               all_responses["engineering"])
        prez_agent.generate_pitch_deck()

    return {"error": "No responses from Agents"}


@app.get("/")
def home():
    return {
        "message":
        "FastAPI server is running!!! Taskss are being processed in sequence."
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
