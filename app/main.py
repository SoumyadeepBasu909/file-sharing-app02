from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

# Initialize the FastAPI app
app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(router)
