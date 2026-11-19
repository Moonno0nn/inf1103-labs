import csv
import json
from pathlib import Path

from product_factory import ProductFactory
from inventory_manager import Inventory
from supplier import Supplier

FILENAME = Path(__file__).with_name("inventory.json")

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

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
                    product = ProductFactory.create(
                        "physical", product_id, name, price, stock, weight=weight
                    )

                elif product_type == "digital":
                    download_size = float(record["download_size"])
                    product = ProductFactory.create(
                        "digital", product_id, name, price, stock, file_size=download_size
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

    # Default products using ProductFactory
    inventory.add_product(
        ProductFactory.create(
            "physical", "P001", "Laptop", 1200.00, 15,
            Supplier("S001", "Tech Supplies Inc.", "techsupplies@email.com"),
            weight=2.5
        )
    )

    inventory.add_product(
        ProductFactory.create(
            "physical", "P002", "Mouse", 25.50, 40,
            Supplier("S001", "Tech Supplies Inc.", "techsupplies@email.com"),
            weight=0.2
        )
    )

    inventory.add_product(
        ProductFactory.create(
            "digital", "D001", "Software", 50.00, 20,
            Supplier("S002", "Digital Downloads Ltd.", "info@digitaldownloads.com"),
            file_size=500
        )
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

        # Check product type by attribute / type
        if hasattr(product, "get_weight"):
            record["type"] = "physical"
            record["weight"] = product.get_weight()

        elif hasattr(product, "get_download_size"):
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

def load_products(path: str, inventory: Inventory, supplier: Supplier = None) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        loaded = 0
        with file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header row
            for line_no, row in enumerate(reader, start=2):
                if not row or len(row) < 5:
                    continue
                try:
                    p_type, p_id, name, price_str, stock_str = [item.strip() for item in row[:5]]
                    price = float(price_str)
                    stock = int(stock_str)
                    product = ProductFactory.create(
                        product_type=p_type,
                        product_id=p_id,
                        name=name,
                        price=price,
                        stock_quantity=stock,
                        supplier=supplier
                    )
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as err:
                    print(f"Row {line_no} skipped ({row}): {err}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
