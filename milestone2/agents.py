# agents.py

import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor

from tools import tools
from memory import memory
from prompts import SYSTEM_PROMPT

load_dotenv()

def create_agent():
    # Initialize Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",            # or "gemini-1.5-pro"
        temperature=0,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # Create ReAct agent
    agent = create_react_agent(
        llm=llm,
        tools=tools
    )

    # Wrap agent in executor with memory and system prompt
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        system_message=SYSTEM_PROMPT
    )

    return agent_executor
