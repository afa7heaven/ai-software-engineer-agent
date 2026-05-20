import requests

API_KEY = "GROQ_API_KEY_KAMU"

def ai_engine(task, mode):

    prompt = f"""
Kamu adalah AI Software Engineer.

MODE:
{mode}

TASK:
{task}

Jawab langsung dan jelas.
"""

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]
