from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

@app.get("/products", response_model=List[Product])
async def get_products():
    """
    Returns a list of products.
    """
    products = [
        {"id": 1, "name": "Laptop", "price": 1200.00},
        {"id": 2, "name": "Mouse", "price": 25.50},
        {"id": 3, "name": "Keyboard", "price": 75.99},
        {"id": 4, "name": "Monitor", "price": 300.00}
    ]
    return products
