def test_context_presence_judge_simple():
    from langchain_community.llms import Ollama
    from tools.context_presence_judge import build_context_presence_tool

    llm = Ollama(model="llama3")
    tool = build_context_presence_tool(llm)
    result = tool.run("What is the capital of France?")
    assert "context_missing" in result.lower() or "context_provided" in result.lower()

def test_web_search_tool():
    from tools.web_search_tool import simple_web_search
    res = simple_web_search("Python programming language")
    assert "Python" in res or "search failed" not in res.lower()
