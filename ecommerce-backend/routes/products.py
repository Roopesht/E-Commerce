from fastapi import APIRouter, HTTPException
from firestore import get_document, get_all_documents

router = APIRouter()


@router.get("/products")
def list_products():
    products = get_all_documents("products")
    return [
        {
            "id": p["id"],
            "name": p.get("name"),
            "description": p.get("description"),
            "price": p.get("price"),
            "image_url": p.get("image_url"),
            "stock": p.get("stock")
        }
        for p in products
    ]


@router.get("/products/{product_id}")
def get_product(product_id: str):
    product = get_document("products", product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "id": product["id"],
        "name": product.get("name"),
        "description": product.get("description"),
        "price": product.get("price"),
        "image_url": product.get("image_url"),
        "stock": product.get("stock"),
    }
