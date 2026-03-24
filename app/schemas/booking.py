from pydantic import BaseModel
from datetime import date

class BookingOut(BaseModel):
    id: int
    vehicle_id: int
    start_date: date
    end_date: date
    total_price: float
    status: str

    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    vehicle_id: int
    start_date: date
    end_date: date