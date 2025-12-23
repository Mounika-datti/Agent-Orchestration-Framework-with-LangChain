from orchestrator import run_pipeline
from dotenv import load_dotenv

load_dotenv()

query = input("Enter your research topic: ")
research, summary = run_pipeline(query)

print("\n--- Research Output ---\n")
print(research)

print("\n--- Summary Output ---\n")
print(summary)
