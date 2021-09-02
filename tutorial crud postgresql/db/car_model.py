from sqlalchemy import Column, String, Integer
from .db_connection import Base, engine

class CarInDB(Base):
    __tablename__ = "car"
    placa = Column(String(50), primary_key = True, unique = True)
    modelo = Column(String(50))
    pasajeros = Column(Integer)

Base.metadata.create_all(bind = engine)