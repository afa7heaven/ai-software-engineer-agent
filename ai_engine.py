from transformers import pipeline
from memory import save_memory, get_memory

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

def ai_engine(task, mode):

    memory = get_memory()

    prompt = f"""
### SYSTEM
Kamu adalah AI Software Engineer.

### MEMORY
{memory}

### MODE
{mode}

### TASK
{task}

### RULES
- jika web app → buat kode lengkap
- jika flutter → buat struktur flutter
- jika debug → jelaskan error + solusi
- jawab detail
"""

    result = pipe(
        prompt,
        max_new_tokens=500,
        temperature=0.7
    )

    output = result[0]["generated_text"]

    save_memory(f"USER: {task}")
    save_memory(f"AI: {output}")

    return output
