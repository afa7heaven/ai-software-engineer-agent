from transformers import pipeline
from memory import save_memory, get_memory

# MODEL AI GRATIS
pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)

def ai_engine(task, mode):

    memory = get_memory()

    prompt = f"""
Kamu adalah AI Software Engineer.

MEMORY:
{memory}

MODE:
{mode}

TASK:
{task}

ATURAN:
- jika web app → buat struktur file
- jika flutter → buat struktur Flutter
- jika debug → jelaskan error + solusi
- jawab detail
"""

    result = pipe(
        prompt,
        max_new_tokens=300
    )

    output = result[0]["generated_text"]

    save_memory(f"USER: {task}")
    save_memory(f"AI: {output}")

    return output
