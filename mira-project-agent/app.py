from fastapi import FastAPI
from pydantic import BaseModel
from graph.mira_graph import mira_graph
import json
import os

app = FastAPI(title="Mira Project Agent")

class MiraRequest(BaseModel):
    trigger: str = "weekly"

@app.post("/run-mira")
def run_mira(request: MiraRequest):
    try:
        result = mira_graph.invoke({})
        return {
            "status": "success",
            "email_sent": result.get("email_sent"),
            "memory_logged": result.get("memory_logged"),
            "summary": result.get("status_summary")
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

@app.get("/logs")
def get_logs():
    log_path = "memory_logs.json"
    if not os.path.exists(log_path):
        return {"status": "error", "message": "No logs found"}

    with open(log_path, "r") as f:
        logs = json.load(f)

    summaries = [entry["summary"] for entry in logs]
    return {
        "status": "success",
        "total_entries": len(summaries),
        "summaries": summaries
    }
