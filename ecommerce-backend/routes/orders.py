from fastapi import APIRouter, HTTPException
from database import db

router = APIRouter()
orders_collection = db["orders"]
cart_collection = db["carts"]


@router.post("orders/place")
def place_order(data:dict):
    username = data["username"]

    cart = cart_collection.find_one({"username": username})

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

    orders_collection.insert_one(order)

    # clear cart after order
    cart_collection.delete_one({"username": username})

    return {"message": "Order placed successfully"}

@router.get("/orders/{username}")
def get_orders(username: str):
    orders =[]

    for order in orders_collection.find({"username": username}):
        orders.append({
            "id": str(order["_id"]),
            "items": order["items"],
            "total_amount": order["total_amount"],
            "status": order["status"]
        })
    return orders
