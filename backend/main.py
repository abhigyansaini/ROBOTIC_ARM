from fastapi import FastAPI

from backend.database.connection import Base, engine

# Import all models so SQLAlchemy knows about them
from backend.models import *

app = FastAPI(
    title="FactoryOps AI",
    version="1.0.0",
    description="Predictive Maintenance and Process Intelligence API"
)

# Create database tables if they don't already exist
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "FactoryOps AI Backend is Running!"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
    