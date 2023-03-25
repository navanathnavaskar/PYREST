import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.patient

patient_collection = database.get_collection("personal")

# Helper
def patient_helper(patient) -> dict :
    return {
        "id": str(patient["_id"]),
        "fullname": patient["fullname"],
        "email": patient["email"],
        "gender": patient["gender"],
        "age": patient["age"],
    }
    
# Get all patients in db
async def get_all_patients():
    patients = []
    async for patient in patient_collection.find():
        patients.append(patient_helper(patient))
    return patients

# Add new patient to db
async def add_patient(patient_data: dict) -> dict :
    patient = await patient_collection.insert_one(patient_data)
    new_patient = await patient_collection.find_one({"_id":patient.inserted_id})
    return patient_helper(new_patient)

# get details of perticular patient
async def get_patient(id: str) -> dict:
    patient = await patient_collection.find_one({"_id":ObjectId(id)})
    if patient:
        return patient_helper(patient)
    
# update patient data
async def update_patient(id: str, patient_data: dict):
    if len(patient_data) < 1:
         return False
    
    patient = await patient_collection.find_one({"_id": ObjectId(id)})
    if patient:
        updated_patient = await patient_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": patient_data}
        )
        if updated_patient:
            return True
        return False
    
    return False

# delete patient data from db
async def delete_patient(id: str):
    patient = await patient_collection.find_one({"_id": ObjectId(id)})
    if patient:
        await patient_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
    