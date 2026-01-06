🎓 Academic Content Assistance System
Multi-Agent AI-Powered Learning Application

📌 Project Description

The Academic Content Assistance System is a student-focused AI application that helps learners quickly understand academic topics.
It uses a multi-agent workflow to automatically research, simplify, summarize, format notes, generate MCQs, and provide downloadable PDFs through a web-based interface.

This project satisfies Milestone 4: Complex Workflow Automation & Evaluation by implementing multi-step automation, multiple collaborating agents, a REST API backend, and an interactive frontend UI.

✨ Features

🔍 Topic-based content generation

🧠 Multi-agent architecture:

Research Agent

Simplification Agent

Summarization Agent

Formatting Agent

MCQ Generator Agent

📘 Simplified explanations

📝 Summary notes

📂 Structured exam notes

🧠 MCQs for self-practice

📄 Download notes as PDF

💾 Topic history storage (SQLite)

🌐 REST API using FastAPI

🖥️ Interactive frontend using Streamlit

🧠 System Workflow

User enters topic
        ↓
Streamlit Frontend (Web App)
        ↓
FastAPI REST API
        ↓
Research Agent
        ↓
Simplification Agent
        ↓
Summarization Agent
        ↓
Formatting Agent
        ↓
MCQ Generator Agent
        ↓
Results displayed to user

🛠️ Technologies Used
Python
LangChain
OpenRouter API
FastAPI
Streamlit
SQLite
ReportLab
REST API
python-dotenv