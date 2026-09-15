from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

app = FastAPI()

# In a real application, this would come from a database
dummy_products = [
    {"id": 1, "name": "Laptop", "price": 1200.00},
    {"id": 2, "name": "Mouse", "price": 25.50},
    {"id": 3, "name": "Keyboard", "price": 75.00},
    {"id": 4, "name": "Monitor", "price": 300.00}
]

@app.get("/products", response_model=list[Product])
async def get_products():
    """Return a list of all products."""
    return dummy_products
