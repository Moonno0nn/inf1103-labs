## Load and save inventory data. 
import json
from pathlib import Path

from product import Product
from inventory_manager import Inventory

FILENAME = Path(__file__).with_name("inventory.json")


def load_inventory():
    """Return an Inventory populated from JSON, or the default products."""
    inventory = Inventory()
    if FILENAME.exists():
        try:
            with FILENAME.open("r", encoding="utf-8") as file:
                records = json.load(file)
            if not isinstance(records, list):
                raise ValueError("Inventory JSON must contain a list of products")
            for record in records:
                inventory.add_product(Product(
                    record["id"], record["name"],
                    float(record["price"]), int(record["stock"])
                ))
            print("Inventory loaded successfully.")
            return inventory
        except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as error:
            print(f"Could not load inventory.json: {error}")
            print("Starting with default inventory instead.")
    else:
        print("inventory.json not found. Starting with default inventory.")

    for product_id, name, price, stock in [
        ("P001", "Laptop", 1200.00, 15),
        ("P002", "Mouse", 25.50, 40),
        ("P003", "Keyboard", 45.00, 25),
    ]:
        inventory.add_product(Product(product_id, name, price, stock))
    return inventory


def save_inventory(inventory):
    """Save an Inventory to inventory.json using the Week 5 JSON format."""
    records = []
    for product in inventory.get_product_id():
        records.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),
        })
    try:
        with FILENAME.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
        print("Inventory saved successfully to inventory.json.")
        return True
    except OSError as error:
        print(f"Failed to save inventory: {error}")
        return False
