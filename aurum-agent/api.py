from fastapi import FastAPI
from tools.auth import router as auth_router
from tools.notifier import router as notifier_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(notifier_router)
