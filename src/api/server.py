"""FastAPI server for Sash API."""

from fastapi import FastAPI
from src.persistence.seed_data import load_seed_data

app = FastAPI(title="Sash API", version="0.17.0")


@app.get("/health")
async def health():
    return {"status": "ok", "version": "0.17.0"}


@app.post("/seed")
async def seed():
    result = load_seed_data()
    return {"seeded": True, "details": result}
