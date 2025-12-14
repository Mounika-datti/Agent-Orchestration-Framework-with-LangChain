# tools.py

import requests
from langchain.tools import tool

# Tool 1 - Greeting
@tool
def greet(name: str) -> str:
    """Use this to greet a person by name."""
    return f"Hello {name}, I am your LangChain Agent!"

# Tool 2 - Weather
@tool
def weather(city: str) -> str:
    """Get current temperature of a city."""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        res = requests.get(url, timeout=10).json()
        temp = res["current_condition"][0]["temp_C"]
        return f"Current temperature in {city} is {temp}°C"
    except Exception as e:
        return f"Could not get weather for {city}: {e}"

# Export tools as a list
tools = [greet, weather]
