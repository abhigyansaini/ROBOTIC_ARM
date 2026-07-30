from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import relationship
from backend.database.connection import Base


class Incident(Base):
    __tablename__ = "incidents"

    incident_id = Column(Integer, primary_key=True, autoincrement=True)

    robot_id = Column(Integer, ForeignKey("robot_arms.robot_id"))

    severity = Column(String(30))

    incident_type = Column(String(100))

    description = Column(String(300))

    resolved = Column(Boolean, default=False)

    incident_time = Column(
    DateTime,
    default=lambda: datetime.now(timezone.utc)
)
    

robot = relationship(
    "RobotArm",
    back_populates="incidents"
)
