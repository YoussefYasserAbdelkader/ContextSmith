from agent.llm_loader import load_llm

def run_agent(user_query: str, document_text: str):
    """Directly query the LLM without any tool-calling."""
    llm = load_llm()
    prompt = f"""
You are an assistant that extracts and summarizes project milestones.
Read the provided document carefully and list the key milestones clearly.

Document:
{document_text}

Question: {user_query}

Answer:
"""
    # Use invoke() instead of run() — works with all models
    response = llm.invoke(prompt)
    return response.content if hasattr(response, "content") else str(response)
