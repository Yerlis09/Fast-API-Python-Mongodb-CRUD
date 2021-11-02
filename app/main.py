from fastapi import FastAPI
from app.routes .product_routes import product
app = FastAPI(title="Product", description="Endpoint", version="1.0.1")
app.include_router(product)
