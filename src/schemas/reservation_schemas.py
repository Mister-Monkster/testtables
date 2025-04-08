from datetime import datetime
from typing import Optional

import pytz
from pydantic import BaseModel, field_validator


class ReservationPostSchema(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: Optional[int] = 60

    @field_validator('reservation_time', mode='before')
    def time_validator(cls, value, ):
        current_datetime = datetime.now()
        timezone_dt = current_datetime.replace(tzinfo=pytz.utc)
        if datetime.fromisoformat(value) < timezone_dt:
            raise ValueError('Нельзя забронировать столик на прошедшую дату.')
        return value

    @field_validator('table_id', mode='before')
    def table_id_validator(cls, value):
        if value <= 0:
            raise ValueError('id Столика должно быть больше 0')
        return value

class ReservationGetSchema(ReservationPostSchema):
    id: int
