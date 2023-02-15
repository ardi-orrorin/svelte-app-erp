from pydantic import BaseModel
from datetime import datetime


class Notification(BaseModel):
    channel: str
    username: str
    message: str
    create_date: datetime
