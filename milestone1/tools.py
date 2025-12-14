# tools.py

import requests
from langchain.tools import tool


@tool
def greet(name: str) -> str:
    """Use this to greet a person by name."""
    return f"Hello {name}, I am your LangChain Agent!"


@tool
def weather(city: str) -> str:
    """Get current temperature of a city."""
    url = f"https://wttr.in/{city}?format=j1"
    res = requests.get(url, timeout=10).json()
    temp = res["current_condition"][0]["temp_C"]
    return f"Current temperature in {city} is {temp}°C"


tools = [greet, weather]
