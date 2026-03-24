from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app.models.booking import Booking
from app.schemas.booking import BookingOut, BookingCreate
from app.core.security import get_current_user
from app.models.user import User 
from app.models.vehicle import Vehicle
from datetime import date

router = APIRouter()


@router.post("/", response_model=BookingOut)
def create_booking(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
): 
    if booking.start_date > booking.end_date: 
        raise HTTPException(status_code=400, detail="Invalid date range")
    
    vehicle = db.query(Vehicle).filter(Vehicle.id == booking.vehicle_id).first() 
    if not vehicle: 
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    existing_booking = db.query(Booking).filter(
        Booking.vehicle_id == booking.vehicle_id,
        Booking.status == "active",
        Booking.start_date <= booking.end_date,
        Booking.end_date >= booking.start_date
    ).first() 

    if existing_booking: 
        raise HTTPException(status_code=400, detail="Vehicle already booked for these dates")
    
    days = (booking.end_date - booking.start_date).days + 1
    total_price = days * vehicle.price_per_day

    new_booking = Booking(
        vehicle_id=booking.vehicle_id,
        user_id=current_user.id,
        start_date=booking.start_date,
        end_date=booking.end_date,
        total_price=total_price,
        status="active"
    )

    db.add(new_booking)

    vehicle = db.query(Vehicle).filter(Vehicle.id == booking.vehicle_id).first()
    if vehicle:
        vehicle.is_available = True
        
    db.commit() 
    db.refresh(new_booking)

    return new_booking

@router.get("/me", response_model=list[BookingOut])
def get_my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Booking).filter(
        Booking.user_id == current_user.id
    ).all()



@router.delete("/{booking_id}", response_model=dict)
def cancel_booking(
    booking_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    if booking.user_id != current_user.id: 
        raise HTTPException(status_code=403, detail="Not authorized")
    
    booking.status = "cancelled"  
    db.commit()

    return {"message": "Booking cancelled"}

