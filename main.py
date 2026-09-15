from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

# Dummy data for products
products_db = [
    {"id": 1, "name": "Laptop", "price": 1200.00},
    {"id": 2, "name": "Mouse", "price": 25.50},
    {"id": 3, "name": "Keyboard", "price": 75.00},
    {"id": 4, "name": "Monitor", "price": 300.00}
]

@app.get("/products", response_model=List[Product])
async def get_products():
    """Return a list of all products."""
    return products_db
