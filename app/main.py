from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth

import app.models.user
import app.models.vehicle
import app.models.booking

from app.routes import booking
from app.routes import vehicle

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(booking.router, prefix="/bookings", tags =["bookings"])
app.include_router(vehicle.router, prefix="/vehicles", tags=["Vehicles"])

@app.get("/")
def root():
    return {"message": "Rental Car API running"}

