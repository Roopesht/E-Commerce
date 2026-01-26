from fastapi import APIRouter, HTTPException
from database import db

router = APIRouter()
cart_collection =db["carts"]
products_collection = db["products"]

@router.post("/cart/add")
def add_to_cart(data: dict):
    username = data["username"]
    product_id = data["product_id"]

    product = products_collection.find_one({"_id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="product Not Found")
    
    cart = cart_collection.find_one({"username": username})

    item = {
        "product_id": product_id,
        "name": product["name"],
        "price": product["price"],
        "quantity": 1
    }

    if not cart:
        cart_collection.insert_one({
            "username": username,
            "items": [item]
        })
    else:
        cart_collection.update_one(
            {"username": username},
            {"$push": {"items": item}}
        )

    return {"message": "Item added to cart"}

@router.get("/cart/{username}")
def view_cart(username:str):
    cart = cart_collection.find_one({"username": username})

    if not cart:
        return {"items": [],
                "message": "Cart is empty"}
    
    return {"items": cart["items"]}