from fastapi import FastAPI, Depends, status, HTTPException
from typing import List
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from db import get_db
from sqlalchemy.orm import Session
from models.sensorModel import SensorsVaccine
from schemas.sensorSchema import SensorsVaccineSchema, SensorsVaccine as SensorsVaccineResponse
app = FastAPI()
bearer_scheme = HTTPBearer()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)
@app.post('/sensorsVaccine', status_code=status.HTTP_201_CREATED, response_model=SensorsVaccineResponse)
def create_user(post_user: SensorsVaccineSchema, db: Session = Depends(get_db)):
    try:
        new_sensorsVaccine = SensorsVaccine(
            measurementUnit=post_user.measurementUnit,
            nameSensor=post_user.nameSensor,
            information=post_user.information
        )
        
        db.add(new_sensorsVaccine)
        db.commit()
        db.refresh(new_sensorsVaccine)

        response = JSONResponse(content={
            "idSensorCheck": new_sensorsVaccine.idSensorsVaccine,
            "measurementUnit": new_sensorsVaccine.measurementUnit,
            "nameSensor": new_sensorsVaccine.nameSensor,
            "information": new_sensorsVaccine.information
        }, status_code=201)

        return response

    except Exception as e:
        db.rollback()  
        raise HTTPException(status_code=500, detail="Error creating sensorVaccines: " + str(e))
