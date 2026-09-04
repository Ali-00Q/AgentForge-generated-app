from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HealthDetails(BaseModel):
    status: str
    service: str
    version: str

@app.get("/health/details", response_model=HealthDetails)
async def get_health_details():
    return {
        "status": "ok",
        "service": "backend",
        "version": "1.0.0"
    }

