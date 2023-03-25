from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class PatientSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    gender: str = Field(...)
    age: int = Field(..., gt=0, lt=100)
    
    class Config:
        schema_extra = {
            "example": {
                "fullname": "Navanath Navaskar",
                "email": "nnavaskar@gmail.com",
                "gender": "male",
                "age": 10,
            }
        }

class UpdatePatientModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    gender: Optional[str]
    age: Optional[int]
    
    class Config:
        schema_extra = {
            "example": {
                "fullname": "Navanath Navaskar",
                "email": "nnavaskar@gmail.com",
                "gender": "male",
                "age": 10,
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }
    