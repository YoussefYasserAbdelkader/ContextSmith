from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import Tool
import json

def build_context_splitter_tool(llm):
    prompt = PromptTemplate.from_template(open("prompts/splitter_prompt.txt").read())
    chain = LLMChain(llm=llm, prompt=prompt)

    def split_message(message):
        raw = chain.run(message)
        try:
            data = json.loads(raw)
            return data
        except:
            return {"context": "", "question": message}

    return Tool.from_function(
        func=split_message,
        name="ContextSplitter",
        description="Splits the message into context and question"
    )
