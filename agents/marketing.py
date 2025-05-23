import os
from typing import Optional
from dotenv import load_dotenv
import requests
from utils.utils import CHAR_LIMIT

load_dotenv()


class MarketingAgent():

  def __init__(self, endpoint=None):
    self.endpoint = endpoint or os.getenv("MARKETING_ENDPOINT")

  def get_response(self,
                   user_idea: str,
                   input_text: str,
                   char_limit=CHAR_LIMIT):

    payload = {
        "instruction": user_idea,
        "input_text": input_text,
        "max_new_tokens": 1024
    }
    try:
        response = requests.post(self.endpoint, json=payload)
        response.raise_for_status()
        response = response.json()
        print(f"Response from Marketing Agent: {response["generated_text"][:char_limit]}")
        return response["generated_text"]
    except Exception as e:
      print(f"Error processing task for Marketing: {e}")
