from fastapi import APIRouter, HTTPException
from database import db
from bson import ObjectId

router = APIRouter()
products_collection = db["products"]


@router.get("/products")
def list_products():
    products = []

    for product in products_collection.find():
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "description": product["description"],
            "price": product["price"],
            "image_url": product["image_url"],
            "stock": product["stock"]
        })

    return products


@router.get("/products/{product_id}")
def get_product(product_id: str):
    try:
        object_id = ObjectId(product_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid product id")

    product = products_collection.find_one({"_id": object_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "id": str(product["_id"]),
        "name": product.get("name"),
        "description": product.get("description"),
        "price": product.get("price"),
        "image_url": product.get("image_url"),
        "stock": product.get("stock"),
    }
