from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="gpt2"
)

def ai_engine(task, mode):
    prompt = f"""
Mode: {mode}
Tugas: {task}
Buat kode aplikasi lengkap.
"""

    result = pipe(prompt, max_new_tokens=300)[0]["generated_text"]
    return result
