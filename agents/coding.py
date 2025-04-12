import os
from typing import Optional
from dotenv import load_dotenv
import requests
from utils.utils import CHAR_LIMIT

load_dotenv()


class CodingAgent():

  def __init__(self, endpoint=None):
    self.endpoint = endpoint or os.getenv("CODING_ENDPOINT")

  def get_response(self, user_idea: str, input_text: str,char_limit = CHAR_LIMIT):

    payload = {"task": input_text}
    
    try:
      response = requests.post(self.endpoint, json=payload)
      response.raise_for_status()
      response = response.json()
      print(f"Response from Coding Agent: {response["generated_text"]}\n")
      return response["generated_text"]

    
    except Exception as e:
      print(f"Error processing task for Coding: {e}")
