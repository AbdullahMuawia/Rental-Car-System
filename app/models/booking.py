from sqlalchemy import Column, Integer, ForeignKey, Date, Float, String
from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    total_price = Column(Float)
    status = Column(String, default="active")