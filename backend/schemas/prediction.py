from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PredictionBase(BaseModel):
    robot_id: int
    failure_probability: float
    predicted_status: str
    recommended_action: Optional[str] = None


class PredictionCreate(PredictionBase):
    pass


class PredictionUpdate(BaseModel):
    failure_probability: Optional[float] = None
    predicted_status: Optional[str] = None
    recommended_action: Optional[str] = None


class PredictionResponse(PredictionBase):
    prediction_id: int
  
    prediction_time: datetime

    model_config = ConfigDict(from_attributes=True)