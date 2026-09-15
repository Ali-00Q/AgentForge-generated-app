from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

# In-memory database of products
products_db: List[Product] = [
    Product(id=1, name="Laptop", price=1200.00),
    Product(id=2, name="Mouse", price=25.50),
    Product(id=3, name="Keyboard", price=75.99),
    Product(id=4, name="Monitor", price=300.00),
    Product(id=5, name="Webcam", price=50.00)
]

@app.get("/products", response_model=List[Product])
async def get_products():
    """
    Retrieve a list of all products.
    """
    return products_db
