# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from models import init_db, SessionLocal
from crud import create_feedback

app = FastAPI()

class FeedbackCreate(BaseModel):
    score: int

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.post("/feedback/")
async def submit_feedback(feedback: FeedbackCreate, db: AsyncSession = Depends(get_db)):
    return await create_feedback(db=db, score=feedback.score)
