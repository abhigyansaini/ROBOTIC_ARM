from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.connection import Base


class Maintenance(Base):
    __tablename__ = "maintenance"

    maintenance_id = Column(Integer, primary_key=True, autoincrement=True)

    robot_id = Column(Integer, ForeignKey("robot_arms.robot_id"))

    maintenance_type = Column(String(50))

    technician = Column(String(100))

    maintenance_date = Column(Date)

    next_due_date = Column(Date)

    remarks = Column(String(300))
    
robot = relationship(
    "RobotArm",
    back_populates="maintenance_records"
)

