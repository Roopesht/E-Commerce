from fastapi import APIRouter, HTTPException
from firestore import get_document, add_document, delete_document, query_documents

router = APIRouter()


@router.post("/orders/place")
def place_order(data: dict):
    username = data["username"]

    cart = get_document("carts", username)

    if not cart or not cart.get("items"):
        raise HTTPException(status_code=400, detail="Cart is empty")

    total_amount = sum(
        item["price"] * item["quantity"] for item in cart["items"]
    )

    order = {
        "username": username,
        "items": cart["items"],
        "total_amount": total_amount,
        "status": "PLACED"
    }

    add_document("orders", order)

    # Clear cart after order
    delete_document("carts", username)

    return {"message": "Order placed successfully"}


@router.get("/orders/{username}")
def get_orders(username: str):
    order_docs = query_documents("orders", "username", "==", username)
    return [
        {
            "id": order["id"],
            "items": order["items"],
            "total_amount": order["total_amount"],
            "status": order["status"]
        }
        for order in order_docs
    ]
