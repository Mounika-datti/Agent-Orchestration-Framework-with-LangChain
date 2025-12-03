from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0
)

# Dummy tool example
def greet(name: str):
    return f"Hello {name}, welcome to Agents powered by Gemini!"

greet_tool = Tool(
    name="greeting_tool",
    func=greet,
    description="Use this tool to greet a person by name."
)

# Create Zero-Shot ReAct Agent
agent = initialize_agent(
    tools=[greet_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run agent
result = agent.run("Greet Saadhana in a friendly way.")
print("\nAgent Response:\n", result)
