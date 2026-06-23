import os

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi.responses import FileResponse
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from agents.extraction_agent import extract_content
from agents.skills_generator import generate_skills


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create folders automatically
os.makedirs("uploads", exist_ok=True)
os.makedirs("generated", exist_ok=True)


class SkillsRequest(BaseModel):
    filename: str


@app.get("/")
def home():
    return {
        "status": "running"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    filepath = f"uploads/{file.filename}"

    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "status": "success",
        "filename": file.filename,
        "message": "File uploaded successfully"
    }

@app.post("/generate-skills")
def generate(req: SkillsRequest):

    filepath = f"uploads/{req.filename}"

    document_text = extract_content(filepath)

    skills_md = generate_skills(document_text)

    output_file = f"generated/{req.filename}_skills.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(skills_md)

    return {
        "status": "success",
        "skills_file": output_file
    }


@app.get("/download/{filename}")
def download(filename: str):

    path = f"generated/{filename}"

    return FileResponse(
        path,
        media_type="text/markdown",
        filename=filename
    )


@app.get("/health")
def health():
    return {
        "status": "ok"
    }