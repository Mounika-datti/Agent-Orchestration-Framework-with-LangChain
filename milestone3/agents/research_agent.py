from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from memory import create_memory
import os

def create_research_agent():
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="""
        You are a Research Agent.
        Research the following topic and list key points clearly.

        Topic: {topic}
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
