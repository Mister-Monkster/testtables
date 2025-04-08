from typing import Optional

from pydantic import BaseModel, field_validator




class TablePostSchema(BaseModel):
    name: str
    seats: Optional[int] = 1
    location: Optional[str] = 'Зал'

    @field_validator('seats', mode='before')
    def seats_is_positive(cls, value):
        if value <= 0:
            raise ValueError('Мест не может быть меньше чем 1')
        return value

class TableGetSchema(TablePostSchema):
    id: int
