from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from pydantic import BaseModel
from docx import Document
import uuid
import os

app = FastAPI()

class TextRequest(BaseModel):
    content: str

@app.post("/generate-doc")
def generate_doc(data: TextRequest):
    doc = Document()
    doc.add_paragraph(data.content)

    filename = f"{uuid.uuid4()}.docx"
    filepath = f"/tmp/{filename}"
    doc.save(filepath)

    return FileResponse(
        path=filepath,
        filename=filename,
        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
