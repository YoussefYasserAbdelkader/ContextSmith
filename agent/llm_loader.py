from langchain_ollama import ChatOllama

def load_llm():
    return ChatOllama(
        model="llama3",
        temperature=0
    )
