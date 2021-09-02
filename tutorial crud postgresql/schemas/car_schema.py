from pydantic import BaseModel

class CarIn(BaseModel):
    placa: str
    modelo: str
    pasajeros: int

    class Config:
        orm_mode = True

class respuesta(BaseModel):
    mensaje:str

