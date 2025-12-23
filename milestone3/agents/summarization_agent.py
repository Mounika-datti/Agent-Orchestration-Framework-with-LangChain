from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from memory import create_memory
import os

def create_summarization_agent():
    prompt = PromptTemplate(
        input_variables=["research"],
        template="""
        You are a Summarization Agent.
        Summarize the following research concisely.

        Research Content:
        {research}
        """
    )

    llm = ChatOpenAI(
        model="mistralai/mistral-7b-instruct",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0.3
    )

    memory = create_memory()
    chain = prompt | llm

    return chain, memory
