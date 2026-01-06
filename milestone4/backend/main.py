from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from orchestrator import academic_workflow
from db import save_topic, get_history
from pdf_utils import generate_pdf

app = FastAPI(title="Academic Content Assistance System")

class TopicRequest(BaseModel):
    topic: str

@app.post("/generate")
def generate(data: TopicRequest):
    save_topic(data.topic)
    return academic_workflow(data.topic)

@app.post("/download-pdf")
def download_pdf(data: TopicRequest):
    result = academic_workflow(data.topic)
    pdf_path = generate_pdf(result["formatted_notes"])
    return FileResponse(pdf_path, filename="notes.pdf")

@app.get("/history")
def history():
    return get_history()
