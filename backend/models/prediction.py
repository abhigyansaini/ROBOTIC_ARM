from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import relationship
from backend.database.connection import Base


class Prediction(Base):
    __tablename__ = "predictions"

    prediction_id = Column(Integer, primary_key=True, autoincrement=True)

    robot_id = Column(Integer, ForeignKey("robot_arms.robot_id"))

    failure_probability = Column(Float)

    predicted_fault = Column(String(100))

    confidence = Column(Float)

    recommended_action = Column(String(200))

    timestamp = Column(
    DateTime,
    default=lambda: datetime.now(timezone.utc)
)
    
robot = relationship(
    "RobotArm",
    back_populates="predictions"
)
