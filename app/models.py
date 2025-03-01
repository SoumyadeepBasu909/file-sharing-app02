from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
import datetime

class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    filepath = Column(String, unique=True)
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)
