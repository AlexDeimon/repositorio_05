from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db
from db.car_model import CarInDB
from schemas.car_schema import CarIn, respuesta

router = APIRouter()

@router.post("/newCar", response_model = CarIn)
def new_car(entrada: CarIn, db:Session = Depends(get_db)):
    try:
        carro = CarInDB(placa = entrada.placa, modelo = entrada.modelo , pasajeros = entrada.pasajeros)
        db.add(carro)
        db.commit()
        db.refresh(carro)
        return carro
    except:
        raise HTTPException(status_code = 404, detail = "El carro ya existe")

@router.get("/allCars", response_model = List[CarIn])
def all_cars(db:Session = Depends(get_db)):
    carros = db.query(CarInDB).order_by(CarInDB.placa).all()
    return carros

@router.get("/searchCar/{placa}", response_model = CarIn)
def search_car(placa: str, db: Session = Depends(get_db)):
    carro = db.query(CarInDB).first()
    if carro == None:
        raise HTTPException(status_code = 404, detail = "El carro no existe")
    else:
        return carro

@router.put("/updateCar", response_model = CarIn)
def update_car(car_act: CarIn, db: Session = Depends(get_db)):
    carro = db.query(CarInDB).get(car_act.placa)

    if carro == None:
        raise HTTPException(status_code = 404, detail = "El carro no existe")

    carro.placa = car_act.placa
    carro.modelo = car_act.modelo
    carro.pasajeros = car_act.pasajeros

    db.commit()
    db.refresh(carro)
    return carro

@router.delete("/deleteCar/{placa}", response_model = respuesta)
def delete_car(placa: str, db: Session = Depends(get_db)):
    carro = db.query(CarInDB).first()
    if carro == None:
        raise HTTPException(status_code = 404, detail = "El carro no existe")
    else:
        db.delete(carro)
        db.commit()
        Respuesta = respuesta(mensaje = "Carro eliminado exitosamente")
        return Respuesta
