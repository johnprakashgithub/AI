from fastapi import FastAPI
from tools.auth import router as auth_router
from tools.notifier import router as notifier_router
from aurum_agent.graph import build_graph

app = FastAPI()
app.include_router(auth_router)
app.include_router(notifier_router)
aurum = build_graph()

@app.post("/run")
def run(payload: dict):
    result = aurum.invoke(payload)
    return result