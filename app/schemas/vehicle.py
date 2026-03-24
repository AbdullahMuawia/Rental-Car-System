from pydantic import BaseModel 

class VehicleCreate(BaseModel):
    brand:str 
    model:str 
    year:int 
    price_per_day:float