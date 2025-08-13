from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import Tool

def build_relevance_checker_tool(llm):
    prompt = PromptTemplate.from_template(open("prompts/relevance_checker_prompt.txt").read())
    chain = LLMChain(llm=llm, prompt=prompt)
    return Tool.from_function(
        func=lambda q: chain.run(q),
        name="ContextRelevanceChecker",
        description="Checks if provided context is relevant to the question"
    )
