# Required installations:
# pip install langchain langchain-google-genai python-dotenv google-generativeai

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# 1️⃣ Connect to Gemini Model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.2
)

# 2️⃣ Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    You are a helpful AI assistant. Explain the topic below
    in very simple, clear, and beginner-friendly language:

    Topic: {topic}
    """
)

# 3️⃣ Create Chain
chain = LLMChain(llm=llm, prompt=prompt)

# 4️⃣ Take input from user
topic_name = input("Enter a topic to explain: ")

# 5️⃣ Run chain
result = chain.invoke({"topic": topic_name})

print("\n--- OUTPUT ---\n")
print(result["text"])
