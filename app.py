from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from docx import Document
import uuid
import os

app = FastAPI()

# 掛載 static 目錄為公開目錄
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

class TextRequest(BaseModel):
    content: str

@app.post("/generate-doc")
def generate_doc(data: TextRequest, request: Request):  # 👈 加入 request
    doc = Document()
    doc.add_paragraph(data.content)

    filename = f"{uuid.uuid4()}.docx"
    filepath = os.path.join("static", filename)
    doc.save(filepath)

    return {
        "url": str(request.base_url) + f"static/{filename}"
    }
