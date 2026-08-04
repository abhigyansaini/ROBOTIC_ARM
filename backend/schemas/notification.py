from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class NotificationBase(BaseModel):
    robot_id: int
    title: str
    message: str
    notification_type: str
    is_read: bool = False


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(BaseModel):
    title: Optional[str] = None
    message: Optional[str] = None
    notification_type: Optional[str] = None
    is_read: Optional[bool] = None


class NotificationResponse(NotificationBase):
    notification_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)