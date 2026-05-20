import streamlit as st
from ai_engine import ai_engine
from memory import get_memory

st.set_page_config(
    page_title="AI Software Engineer",
    layout="wide"
)

st.title("🤖 AI Software Engineer")

st.sidebar.title("🧠 Memory")

st.sidebar.text(get_memory())

mode = st.selectbox("Mode", [
    "Full Stack Web App",
    "Mobile App (Flutter)",
    "Debug Error"
])

task = st.text_area(
    "Masukkan tugas AI:"
)

if st.button("🚀 Generate"):

    with st.spinner("AI sedang bekerja..."):

        result = ai_engine(task, mode)

    st.subheader("📦 Hasil AI")

    st.code(result)

    st.download_button(
        "⬇ Download Result",
        result,
        file_name="ai_output.txt"
    )
