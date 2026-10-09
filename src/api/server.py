"""FastAPI server for Sash API."""

from fastapi import FastAPI
from src.persistence.seed_data import seed_mock_data

app = FastAPI(title="Sash API")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/seed")
async def seed():
    seed_mock_data()
    return {"seeded": True}
