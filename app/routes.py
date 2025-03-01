from fastapi import APIRouter, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import UploadedFile
import shutil, os

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Save file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Store file metadata in database
    db = SessionLocal()
    db_file = UploadedFile(filename=file.filename, filepath=file_path)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    db.close()

    return {"message": "File uploaded", "file_id": db_file.id}

@router.get("/download/{file_id}")
async def download_file(file_id: int):
    db = SessionLocal()
    file_record = db.query(UploadedFile).filter(UploadedFile.id == file_id).first()
    db.close()

    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")

    return {"download_url": f"http://localhost:8000/static/{file_record.filename}"}
