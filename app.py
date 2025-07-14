from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from docx import Document
import io

app = FastAPI()

class TextRequest(BaseModel):
    content: str

@app.post("/generate-doc")
def generate_doc(data: TextRequest):
    doc = Document()
    doc.add_paragraph(data.content)

    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f"attachment; filename=generated.docx"}
    )
