from pydantic import BaseModel


class HealthRequest(BaseModel):
    temperature: float
    vibration: float
    current: float
    torque: float


class HealthResponse(BaseModel):
    health_score: float
    health_status: str