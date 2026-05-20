from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# model gratis
pipe = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1"
)

llm = HuggingFacePipeline(pipeline=pipe)

template = """
Kamu adalah AI Software Engineer.

Mode: {mode}

Tugas:
{task}

ATURAN:
- buat full stack jika web
- buat Flutter jika mobile
- jelaskan error jika debugging
"""

prompt = PromptTemplate(
    input_variables=["mode", "task"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

def ai_engine(task, mode):
    result = chain.run({"mode": mode, "task": task})
    return result
