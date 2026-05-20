import streamlit as st
from ai_engine import ai_engine
from memory import load_memory

st.set_page_config(page_title="AI Software Engineer Agent", layout="wide")

st.title("🤖 AI Software Engineer Agent")

mode = st.selectbox("Mode AI", [
    "Full Stack Web App",
    "Mobile App (Flutter)",
    "Debug Error"
])

prompt = st.text_area("Masukkan instruksi:")

if st.button("🚀 Generate"):
    result = ai_engine(prompt, mode)

    st.subheader("📦 Hasil AI")
    st.code(result)

    st.download_button(
        "⬇ Download Code",
        result,
        file_name="project.txt"
    )

st.sidebar.subheader("🧠 Memory")
st.sidebar.text(load_memory())
