from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from docx import Document
import uuid
import os

app = FastAPI()

class TextRequest(BaseModel):
    content: str

# 假設這個資料夾有對外開放存取（例如 Zeabur 的 /static 資料夾）
STATIC_FOLDER = "/app/static"
PUBLIC_URL_PREFIX = "https://dify-word.zeabur.app/static"

@app.post("/generate-doc")
def generate_doc(data: TextRequest):
    doc = Document()
    doc.add_paragraph(data.content)

    filename = f"{uuid.uuid4()}.docx"
    filepath = os.path.join(STATIC_FOLDER, filename)
    doc.save(filepath)

    download_url = f"{PUBLIC_URL_PREFIX}/{filename}"
    return JSONResponse(content={"download_url": download_url})
