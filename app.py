import streamlit as st
from transformers import pipeline

st.title("🤖 AI Software Engineer")

pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)

mode = st.selectbox("Mode", [
    "Web App",
    "Flutter",
    "Debug"
])

task = st.text_area("Masukkan tugas")

if st.button("Generate"):

    prompt = f"""
Mode: {mode}

Task:
{task}
"""

    result = pipe(
        prompt,
        max_new_tokens=200
    )

    st.subheader("📦 Hasil AI")

    st.code(result[0]["generated_text"])
