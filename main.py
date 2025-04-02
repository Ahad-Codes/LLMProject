from fastapi import FastAPI
import httpx
from pydantic import BaseModel
from typing import Dict, Any
import asyncio
from projectman import ProjectManagerAgent
import os
from dotenv import load_dotenv
import requests
from write_docs import write_docx
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()


AGENT_ENDPOINTS = {
    "legal": "https://3a1d-34-83-115-121.ngrok-free.app/generate",
    "marketing": "https://3756-34-143-131-109.ngrok-free.app/generate",
    "engineering": "https://bb83-129-10-8-207.ngrok-free.app/generate"
}

class TaskRequest(BaseModel):
    tasks: Dict[str, Dict[str, Any]]

@app.post("/tasks")
async def process_tasks():
            
    pm_agent = ProjectManagerAgent()

    #dummy User Input
    company_name, user_idea = ["VentureMarket", "An AI-powered chatbot that helps small businesses create automated marketing content."]

    structured_tasks = pm_agent.get_response(user_idea, type_s="task")

    all_responses = {}

    for agent, task_data in structured_tasks.items():
            if agent in AGENT_ENDPOINTS:
                try:
                    print(f"Waiting for response from {agent}...")
                    agent_url = AGENT_ENDPOINTS[agent]
                    response = requests.post(agent_url, json={"task" : task_data})
                    response.raise_for_status()  
                    response = response.json()
                    
                    print(f"🔍 Response from {agent}: \n\n {response} : {type(response)}")
                    all_responses[agent] = response["response_text"]
                except Exception as e:
                    print(f"Error processing task for {agent}: {e}")

    for agent, response in all_responses.items():
         if agent == "marketing" or agent == "legal":
                print('Sending Gemma and Mistral for Formatting...')
                check = pm_agent.get_response(response, type_s="format")
                print(check)
                with open("outputs/format.json", "w") as f:
                    json.dump(check, f)

                all_responses[agent] = check
    
    write_docx(all_responses, name = company_name, idea = user_idea)

    print("✅ Responses from Agents completed.")
    return all_responses  

@app.get("/")
def home():
    return {"message": "FastAPI server is running. Tasks are being processed in sequence."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


