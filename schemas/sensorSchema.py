from pydantic import BaseModel
from typing import Optional

class SensorsVaccineSchema(BaseModel):
  amountVaccines : int
  measurementUnit : str
  nameSensor : str
  information : str
class SensorsVaccine(SensorsVaccineSchema):
    idSensorVaccine : int
    
    class Config:
        orm_mode : True