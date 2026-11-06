
import json
from pathlib import Path

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory_manager import Inventory


FILENAME = Path(__file__).with_name("inventory.json")


def load_inventory():
    """Load physical and digital products from JSON."""
    inventory = Inventory()

    if FILENAME.exists():
        try:
            with FILENAME.open("r", encoding="utf-8") as file:
                records = json.load(file)

            if not isinstance(records, list):
                raise ValueError("Inventory JSON must contain a list.")

            products = []

            for record in records:
                product_type = record["type"]

                product_id = record["id"]
                name = record["name"]
                price = float(record["price"])
                stock = int(record["stock"])

                if product_type == "physical":
                    weight = float(record["weight"])

                    product = PhysicalProduct(
                        product_id, name, price, stock, weight
                    )

                elif product_type == "digital":
                    download_size = float(record["download_size"])

                    product = DigitalProduct(
                        product_id, name, price, stock, download_size
                    )

                else:
                    raise ValueError(
                        f"Unknown product type: {product_type}"
                    )

                products.append(product)

            for product in products:
                inventory.add_product(product)

            print("Inventory loaded successfully.")
            return inventory

        except (OSError, ValueError, TypeError, KeyError) as error:
            print(f"Could not load inventory.json: {error}")
            print("Starting with default inventory instead.")

    else:
        print("inventory.json not found. Starting with default inventory.")

    # Default products
    inventory.add_product(
        PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5)
    )

    inventory.add_product(
        PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2)
    )

    inventory.add_product(
        DigitalProduct("D001", "Software", 50.00, 20, 500)
    )

    return inventory


def save_inventory(inventory):
    """Save physical and digital products to JSON."""
    records = []

    for product in inventory.get_products():

        record = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        }

        if isinstance(product, PhysicalProduct):
            record["type"] = "physical"
            record["weight"] = product.get_weight()

        elif isinstance(product, DigitalProduct):
            record["type"] = "digital"
            record["download_size"] = product.get_download_size()

        else:
            print("Error: Unsupported product type.")
            return False

        records.append(record)

    try:
        with FILENAME.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

        print("Inventory saved successfully to inventory.json.")
        return True

    except OSError as error:
        print(f"Failed to save inventory: {error}")
        return False
