"""
Standalone script to manually add products to Firestore.
Not exposed as an API endpoint for security reasons.
Run this file directly: python routes/add_products.py
"""

import sys
import os

# Add parent directory to path so we can import firestore module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from firestore import get_document, add_document


def add_product_manually():
    """Take product details via terminal input and add to Firestore."""
    name = input("Enter product name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    description = input("Enter product description: ").strip()

    try:
        price = float(input("Enter product price: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    image_url = input("Enter product image URL: ").strip()

    try:
        stock = int(input("Enter product stock quantity: "))
    except ValueError:
        print("Invalid stock quantity. Please enter a whole number.")
        return

    # If product with same name exists, just increase the stock quantity
    existing_product = get_document("products", name)
    if existing_product:
        existing_stock = existing_product.get("stock", 0)
        new_stock = existing_stock + stock
        add_document("products", {"stock": new_stock}, doc_id=name)
        print(f"Existing product found. Stock updated to {new_stock}")
        return

    product_doc = {
        "name": name,
        "description": description,
        "price": price,
        "image_url": image_url,
        "stock": stock
    }

    add_document("products", product_doc, doc_id=name)
    print("Product added successfully")


if __name__ == "__main__":
    add_product_manually()