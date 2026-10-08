import json
import os

FILENAME = "inventory.json"


def load_inventory():
    """Loads inventory data from inventory.json if it exists, or returns default items."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                print("inventory.json found.")
                print("Inventory loaded successfully.\n")
                return json.load(file)
        except Exception as e:
            print(f"Error loading inventory file: {e}")
            return []
    else:
        print("inventory.json not found. Starting with default inventory.\n")
        # Default starting inventory with at least three products
        return [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
        ]


def save_inventory(inventory):
    """Saves the inventory list to inventory.json."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully to inventory.json.")
    except Exception as e:
        print(f"Failed to save inventory: {e}")


def display_all(inventory):
    """Displays all products in the inventory."""
    print("\nCurrent Inventory")
    print("-" * 35)
    if not inventory:
        print("No products available.")
    else:
        for product in inventory:
            print(
                f"ID:{product['id']}|Name:{product['name']}|Price:${product['price']:.2f}|Stock:{product['stock']}"
            )
    print("-" * 35)


def add_product(inventory):
    """Adds a new product to the inventory."""
    print("\nAdd New Products")
    product_id = input("Product ID: ").strip()

    # Check for duplicate ID
    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("Error: A product with this ID already exists.")
            return

    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid input for price or stock quantity. Product not added.")
        return

    new_product = {"id": product_id, "name": name, "price": price, "stock": stock}

    inventory.append(new_product)
    print("\nProduct added successfully!")


def update_stock(inventory):
    """Updates the stock quantity of an existing product."""
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("\nProduct Found:")
            print(f"Name:{product['name']}")
            print(f"Current Stock: {product['stock']}\n")
            try:
                new_stock = int(input("New Stock Quantity: "))
                product["stock"] = new_stock
                print("\nStock updated successfully!")
            except ValueError:
                print("Invalid stock number. Update cancelled.")
            return

    print("\nProduct not found.")


def search_product(inventory):
    """Searches for a product by its ID."""
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["id"].lower() == product_id.lower():
            print("\nProduct Found")
            print("-" * 30)
            print(f"ID:{product['id']}")
            print(f"Name:{product['name']}")
            print(f"Price:${product['price']:.2f}")
            print(f"Stock:{product['stock']}")
            print("-" * 30)
            return

    print("\nProduct not Found")


def main():
    print("===============================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===============================\n")

    # Load persistent data or default list
    inventory = load_inventory()

    while True:
        print("\n------MENU---------------------")
        print("1.Display All Products")
        print("2.Add Products")
        print("3.Update Stock")
        print("4.Search Products")
        print("5.Save Inventory")
        print("6.Exit")
        print("--------------------------------")

        choice = input("\nEnter Option: ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("\nSaving Inventory...")
            save_inventory(inventory)
        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()