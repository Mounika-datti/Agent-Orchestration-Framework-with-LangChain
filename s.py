import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("GEMINI_API_KEY not found in .env file!")

# Configure Gemini
genai.configure(api_key=api_key)

# Select a working model from your list
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Example messages
messages = [
    {"role": "user", "content": "You are a helpful AI Assistant."},
    {"role": "user", "content": "Explain machine learning in simple terms."}
]

# Convert messages to prompt
prompt = "\n".join([msg["content"] for msg in messages])

# Generate response
response = model.generate_content(prompt)

# Print AI response
print("\n🤖 Gemini Response:\n")
print(response.text)
