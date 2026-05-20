from groq import Groq
import streamlit as st

from memory import save_memory, get_memory

client = Groq(
    api_key="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"
)

def ai_engine(task, mode):

    memory = get_memory()

    prompt = f"""
Kamu adalah AI Software Engineer professional.

MODE:
{mode}

TASK:
{task}

ATURAN:
- jawab langsung
- jangan ulang prompt
- jika coding → tampilkan kode lengkap
- gunakan struktur professional
- gunakan markdown code block
"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama3-70b-8192"
    )

    output = chat_completion.choices[0].message.content

    save_memory(f"USER: {task}")
    save_memory(f"AI: {output}")

    return output
