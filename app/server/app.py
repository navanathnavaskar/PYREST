from fastapi import FastAPI
from app.server.routes.patient import router as PRouter

app = FastAPI()
app.include_router(PRouter, tags=["Patient"], prefix="/patient")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Hospital!"}