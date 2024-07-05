import requests
from src.config import OLLAMA_API_URL, OLLAMA_MODEL

def ask_question(question):
    response = requests.post(
        OLLAMA_API_URL,
        json={"model": OLLAMA_MODEL, "prompt": question, "stream": False }
    )
    response_data = response.json()
    return response_data["response"]
