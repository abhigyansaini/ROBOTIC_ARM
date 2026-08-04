from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TelemetryBase(BaseModel):
    robot_id: int
    temperature: Optional[float] = None
    vibration: Optional[float] = None
    motor_current: Optional[float] = None
    voltage: Optional[float] = None
    power_consumption: Optional[float] = None
    torque: Optional[float] = None
    speed_rpm: Optional[float] = None
    operating_hours: Optional[float] = None
    humidity: Optional[float] = None


class TelemetryCreate(TelemetryBase):
    pass


class TelemetryUpdate(BaseModel):
    temperature: Optional[float] = None
    vibration: Optional[float] = None
    motor_current: Optional[float] = None
    voltage: Optional[float] = None
    power_consumption: Optional[float] = None
    torque: Optional[float] = None
    speed_rpm: Optional[float] = None
    operating_hours: Optional[float] = None
    humidity: Optional[float] = None


class TelemetryResponse(TelemetryBase):
    telemetry_id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)