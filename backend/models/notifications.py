from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import relationship
from backend.database.connection import Base


class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column(Integer, primary_key=True, autoincrement=True)

    robot_id = Column(Integer, ForeignKey("robot_arms.robot_id"))

    alert_type = Column(String(100))

    message = Column(String(300))

    priority = Column(String(30))

    status = Column(String(30))

    created_at = Column(
    DateTime,
    default=lambda: datetime.now(timezone.utc)
)
    

robot = relationship(
    "RobotArm",
    back_populates="notifications" # back_populates means Both objects know about each other
)

