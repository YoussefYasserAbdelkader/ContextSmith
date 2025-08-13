from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import Tool

def build_context_presence_tool(llm, document_text=None):
    """
    Creates a tool that checks if the user input already contains enough context
    to answer the question. If a document is loaded, that is considered context.
    """

    prompt_text = """
    You are a Context Presence Judge.
    You will receive the user’s question and possibly some document text.

    If the question includes enough background information (or if the document text is provided),
    respond with EXACTLY:
    context_provided

    Otherwise, respond with:
    context_missing

    ---
    Document: {document}
    Question: {input}
    """

    prompt = PromptTemplate(
        template=prompt_text,
        input_variables=["document", "input"]
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    def judge_with_input(user_query: str):
        # Pass both the loaded document and the user query
        return chain.run({"document": document_text or "", "input": user_query})

    return Tool.from_function(
        func=judge_with_input,
        name="ContextPresenceJudge",
        description="Checks if the question already has enough context to answer"
    )
