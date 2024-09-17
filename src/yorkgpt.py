from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="yorkgpt/yorkgpt",
    temperature=0.5,
    base_url="http://localhost:11434",
)

def get_model_response(question) :

    template = """Question: {question}
    Answer: Let's think step by step."""

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm
    
    result = chain.invoke({"question": question})

    return result.content if hasattr(result, 'content') else None