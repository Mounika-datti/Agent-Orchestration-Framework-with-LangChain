from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import uuid

def generate_pdf(content):
    os.makedirs("generated_pdfs", exist_ok=True)
    filename = f"notes_{uuid.uuid4().hex}.pdf"
    path = os.path.join("generated_pdfs", filename)

    c = canvas.Canvas(path, pagesize=A4)
    text = c.beginText(40, 800)

    for line in content.split("\n"):
        text.textLine(line)

    c.drawText(text)
    c.save()
    return path
