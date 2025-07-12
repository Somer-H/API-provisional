from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base 

class SensorsVaccine(Base):
    __tablename__ = "sensorsvaccine"
    
    idSensorCheck = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    measurementUnit = Column(String, nullable=True)
    nameSensor = Column(String, nullable=True)
    information = Column(String, nullable=True)