from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[str]
    category: str
    product_name: str
    product_price: float
    product_description: str
