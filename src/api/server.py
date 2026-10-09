"""FastAPI server for Sash API."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.workflow.engine import WorkflowEngine

from src.workflow.designer import create_sample_workflow

app = FastAPI(title="Sash API", version="0.17.0")


class RunWorkflowRequest(BaseModel):
    to: str = "+12065550123"
    correlation_id: str | None = None


class RunWorkflowResponse(BaseModel):
    correlation_id: str
    final_status: str
    event_count: int
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
