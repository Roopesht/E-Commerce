from fastapi import APIRouter, HTTPException
from firestore import get_document, add_document, update_document
from google.cloud.firestore_v1 import ArrayUnion

router = APIRouter()


@router.post("/cart/add")
def add_to_cart(data: dict):
    username = data["username"]
    product_id = data["product_id"]

    product = get_document("products", product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found")

    item = {
        "product_id": product_id,
        "name": product["name"],
        "price": product["price"],
        "quantity": 1
    }

    # Use username as cart document ID
    cart = get_document("carts", username)

    if not cart:
        add_document("carts", {"username": username, "items": [item]}, doc_id=username)
    else:
        update_document("carts", username, {"items": ArrayUnion([item])})

    return {"message": "Item added to cart"}


@router.get("/cart/{username}")
def view_cart(username: str):
    cart = get_document("carts", username)

    if not cart:
        return {"items": [], "message": "Cart is empty"}

    return {"items": cart["items"]}