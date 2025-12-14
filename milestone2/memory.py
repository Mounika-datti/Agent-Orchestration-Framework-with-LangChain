# memory.py

from langchain.memory import ConversationBufferMemory

# Conversation memory for the agent
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
