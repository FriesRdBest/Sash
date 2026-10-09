# Sash API server (optional lightweight wrapper)

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


@app.get("/health")
async def health():
    return {"status": "ok", "version": "0.17.0"}


@app.post("/workflows/run", response_model=RunWorkflowResponse)
async def run_workflow(req: RunWorkflowRequest):
    workflow = create_sample_workflow()
    engine = WorkflowEngine()
    corr_id = req.correlation_id or f"corr_api_{engine._counter}"
    try:
        result = engine.execute(workflow=workflow, to=req.to, correlation_id=corr_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
    return RunWorkflowResponse(
        correlation_id=corr_id,
        final_status=result.final_status,
        event_count=len(result.events),
    )
