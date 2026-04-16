import requests
import os
from dotenv import load_dotenv

load_dotenv()

def ask_ai(prompt):
    API_KEY = os.getenv("API_KEY")

    # you can chose any API base url but also choose the model accordingly
    url = "https://generativelanguage.googleapis.com/v1beta/openai/v1/chat/completions"

    headers={
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"

    }

    data = {
        "model":"gemini-2.5-flash-lite",
        "messages":[
            {
                "role":"user",
                "content":prompt
            }
        ]
    }

    response = requests.post(url=url,
                             headers=headers,
                             json=data)
    reply = response.json()

    if "choices" in reply:
        answer = reply["choices"][0]
        if "message" in answer:
            return answer["message"]["content"]
    elif "error" in reply:
        return reply["error"]["message"]



