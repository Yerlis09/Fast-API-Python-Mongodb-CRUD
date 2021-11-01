def productEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "category": item["category"],
        "product_name": item["product_name"],
        "product_price": item["product_price"],
        "product_description": item["product_description"]
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]
