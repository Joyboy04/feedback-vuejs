# crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from models import Feedback

async def create_feedback(db: AsyncSession, score: int):
    feedback = Feedback(score=score)
    db.add(feedback)
    await db.commit()
    await db.refresh(feedback)
    return feedback
