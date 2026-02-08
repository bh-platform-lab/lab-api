from fastapi import FastAPI
from app.api.v1.routes import router as v1_router

app = FastAPI(title="lab-api", version="0.1.0")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

app.include_router(v1_router, prefix="/api/v1")
