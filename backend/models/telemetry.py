from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from datetime import datetime,timezone
from sqlalchemy.orm import relationship
from backend.database.connection import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    telemetry_id = Column(Integer, primary_key=True, autoincrement=True)

    robot_id = Column(Integer, ForeignKey("robot_arms.robot_id"))

    temperature = Column(Float)
    vibration = Column(Float)
    motor_current = Column(Float)
    voltage = Column(Float)
    power_consumption = Column(Float)
    torque = Column(Float)
    speed_rpm = Column(Float)
    operating_hours = Column(Float)

    timestamp = Column(
    DateTime,
    default=lambda: datetime.now(timezone.utc)
)
# relationship 
robot = relationship(
    "RobotArm",
    back_populates="telemetry_records"
)


    