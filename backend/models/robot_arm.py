from sqlalchemy import Column, Integer, String, Date
from backend.database.connection import Base 
from sqlalchemy.orm import relationship

class RobotArm(Base):
    __tablename__ = "robot_arms"
    
    robot_id = Column(Integer, primary_key=True, autoincrement=True)
    robot_name = Column(String(50), nullable=False, unique=True)
    manufacturer = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    installation_date = Column(Date)
    location = Column(String(100))
    status = Column(String(20), default="Active")
    
# used for relationships one to many
telemetry_records = relationship(
    "Telemetry",
    back_populates="robot",
    cascade="all, delete-orphan"
)

predictions = relationship(
    "Prediction",
    back_populates="robot",
    cascade="all, delete-orphan"
)

maintenance_records = relationship(
    "Maintenance",
    back_populates="robot",
    cascade="all, delete-orphan"
)

incidents = relationship(
    "Incident",
    back_populates="robot",
    cascade="all, delete-orphan"
)

notifications = relationship(
    "Notification",
    back_populates="robot",
    cascade="all, delete-orphan"
)

