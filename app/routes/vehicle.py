from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate
from datetime import date 
from app.models.booking import Booking

router = APIRouter()


@router.post("/")
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    new_vehicle = Vehicle(**vehicle.dict())
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle

@router.get("/")
def list_vehicles(db: Session = Depends(get_db)):
    return db.query(Vehicle).all()

@router.get("/{vehicle_id}/availability")
def check_availability(
    vehicle_id: int, 
    start_date: date, 
    end_date: date, 
    db:Session = Depends(get_db)
):
    if start_date > end_date: 
        raise HTTPException(status_code=400, detail="Invalid date range")
    
    booking = db.query(Booking).filter(
        Booking.vehicle_id == vehicle_id, 
        Booking.status == "active", 
        Booking.start_date <= end_date, 
        Booking.end_date >= start_date
    ).first() 

    if booking: 
        return{
            "available": False, 
            "message": "Vehicle is NOT available for these dates"
        }
    
    return {
            "available": True,
            "message": "Vehicle is available"
        }


@router.get("/")
def get_vehicles(
    min_price: float = 0, 
    max_price:float = 100000,
    db:Session = Depends(get_db)

):
    return db.query(Vehicle).filter(
        Vehicle.price_per_day >= min_price, 
        Vehicle.price_per_day <= max_price
    ).all()



@router.get("/available")
def get_available_vehicles(
    start_date: date,
    end_date: date,
    db: Session = Depends(get_db)
):
    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Invalid date range")

    vehicles = db.query(Vehicle).all()
    available_vehicles = []

    for vehicle in vehicles:
        conflict = db.query(Booking).filter(
            Booking.vehicle_id == vehicle.id,
            Booking.status == "active",
            Booking.start_date <= end_date,
            Booking.end_date >= start_date
        ).first()

        if not conflict:
            available_vehicles.append(vehicle)

    return available_vehicles