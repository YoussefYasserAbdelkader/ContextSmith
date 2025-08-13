import wikipedia
from langchain.tools import Tool

def web_search(query):
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except Exception as e:
        return f"Search failed: {e}"

def build_web_search_tool():
    return Tool.from_function(
        func=web_search,
        name="WebSearchTool",
        description="Searches Wikipedia for missing context"
    )
