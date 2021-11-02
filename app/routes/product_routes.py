# APIRouters
from fastapi import APIRouter
from app.config.db import client
from app.schema.product_schema import productEntity, productsEntity
from app.models.product_model import Product
from bson import ObjectId
from fastapi import HTTPException
product = APIRouter()


@product.post("/user/products", response_model=Product, tags=["Products"])
async def create_product(product: Product):
    id = client.local.product.insert_one(dict(product)).inserted_id
    product = client.local.product.find_one({"_id": ObjectId(id)})
    return productEntity(product)


@product.get("/user/products", response_model=list[Product], tags=["Products"])
async def return_all_product():
    return productsEntity(client.local.product.find())


@product.put("/user/products/{id}", response_model=Product, tags=["Products"])
async def update_product(id: str, product: Product):
    client.local.product.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(product)})
    return productEntity(client.local.product.find_one({"_id": ObjectId(id)}))


@product.delete("/user/products/{id}", tags=["Products"])
async def delete_product(id: str):
    if ObjectId.is_valid(id) and client.local.product.find_one({"_id": ObjectId(id)}):
        productEntity(client.local.product.find_one_and_delete(
            {"_id": ObjectId(id)}))
        return {"message": "Product deleted successfully"}
    else:
        return HTTPException(404, "Product not found")


@product.get("/user/products/total", tags=["Products"])
async def count_all_product():
    return {"total": client.local.product.find().count()}
