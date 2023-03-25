from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_patient,
    delete_patient,
    get_all_patients,
    get_patient,
    update_patient,
)

from app.server.models.patient import (
    ErrorResponseModel,
    ResponseModel,
    PatientSchema,
    UpdatePatientModel,
)

router = APIRouter()

@router.post("/", response_description="Patient data added into DB successfully")
async def add_patient_data(patient: PatientSchema = Body(...)):
    patient = jsonable_encoder(patient)
    new_patient = await add_patient(patient)
    return ResponseModel(new_patient, "Patient added Successfully")

@router.get("/", response_description="All Patients Information")
async def get_all_patient_data():
    patients = await get_all_patients()
    if patients:
        return ResponseModel(patients, "Patients data retrived successfully")
    return ResponseModel(patients, "Empty list returned")

@router.get("/{id}", response_description="Get data of Patient with ID")
async def get_patient_data(id):
    patient = await get_patient(id)
    if patient:
        return ResponseModel(patient, "Successfully retrieved patient information")
    return ErrorResponseModel("Error Occurred", 500, "Patient does not exist.")

@router.put("/{id}")
async def update_patient_data(id, req: UpdatePatientModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_patient = await update_patient(id, req)
    if update_patient:
        return ResponseModel(
            "Patient with ID {} updated successfully".format(id),
            "Patient record updated successfully."
        )
    
    return ErrorResponseModel(
        "An Error Occurred",
        500,
        "Failed to update Patient record",
    )

@router.delete("/{id}", response_description="Patient data deleted successfully")
async def delete_patient_data(id):
    deleted_student = await delete_patient(id)
    if delete_patient:
        return ResponseModel(
            "Patient with ID {} removed successfully".format(id),
            "Patient deleted successfully"
        )
    
    ErrorResponseModel(
        "An Error Occrrued",
        500,
        "Failed to delete patient record."
    )

