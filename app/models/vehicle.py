from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
    price_per_day = Column(Float)
    is_available = Column(Boolean, default=True)