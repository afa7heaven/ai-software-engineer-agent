import anthropic
import streamlit as st
from memory import save_memory, get_memory

client = anthropic.Anthropic(
    api_key=st.secrets["ANTHROPIC_API_KEY"]
)

def ai_engine(prompt, mode):
    memory = get_memory()

    system_prompt = f"""
Kamu adalah AI Software Engineer.

MODE: {mode}

MEMORY:
{memory}

TUGAS:
{prompt}

ATURAN:
- jika web app → full stack
- jika mobile → Flutter Android + iOS
- jika error → debug & fix
"""

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=4000,
        messages=[{"role": "user", "content": system_prompt}]
    )

    result = response.content[0].text

    save_memory(prompt)
    save_memory(result)

    return result
