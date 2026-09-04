from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Customer(BaseModel):
    id: int
    name: str
    email: str

# Dummy data for customers
dummy_customers = [
    {"id": 1, "name": "Alice Smith", "email": "alice.smith@example.com"},
    {"id": 2, "name": "Bob Johnson", "email": "bob.johnson@example.com"},
    {"id": 3, "name": "Charlie Brown", "email": "charlie.brown@example.com"}
]

@app.get("/customers", response_model=List[Customer])
async def get_customers():
    """Returns a list of all customers."""
    return dummy_customers
