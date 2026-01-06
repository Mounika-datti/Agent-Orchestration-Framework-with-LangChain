import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model=os.getenv("OPENROUTER_MODEL"),
    temperature=0.3,
    max_tokens=900,
    default_headers={
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Academic Assistant"
    }
)
