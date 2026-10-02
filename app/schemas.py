from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class UserPlan(Base):
    __tablename__ = "user_plans"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    goal = Column(String(100), nullable=False)
    dietary_pref = Column(String(100), nullable=False)
    workout_plan = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)