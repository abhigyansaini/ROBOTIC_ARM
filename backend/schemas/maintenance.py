from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MaintenanceBase(BaseModel):
    robot_id: int
    maintenance_type: str
    description: Optional[str] = None
    maintenance_date: date
    next_due_date: Optional[date] = None
    technician_name: str
    maintenance_status: str


class MaintenanceCreate(MaintenanceBase):
    pass


class MaintenanceUpdate(BaseModel):
    maintenance_type: Optional[str] = None
    description: Optional[str] = None
    maintenance_date: Optional[date] = None
    next_due_date: Optional[date] = None
    technician_name: Optional[str] = None
    maintenance_status: Optional[str] = None


class MaintenanceResponse(MaintenanceBase):
    maintenance_id: int

    model_config = ConfigDict(from_attributes=True)