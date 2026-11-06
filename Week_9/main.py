
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory_manager import Inventory
from file_manager import load_inventory, save_inventory


def main():
    print("===============================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===============================")

    # Load inventory from JSON
    inventory = load_inventory()

    while True:
        print("\n------ MENU ------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("------------------")

        choice = input("Enter Option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            print("\nSelect Product Type:")
            print("1. Physical Product")
            print("2. Digital Product")

            product_type = input("Enter Product Type: ").strip()

            if product_type not in ("1", "2"):
                print("Invalid product type.")
                continue

            product_id = input("Product ID: ").strip()
            name = input("Product Name: ").strip()

            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))

                if price < 0 or stock < 0:
                    print("Price and stock cannot be negative.")
                    continue

                if product_type == "1":
                    weight = float(input("Weight (kg): "))

                    if weight < 0:
                        print("Weight cannot be negative.")
                        continue

                    new_product = PhysicalProduct(
                        product_id, name, price, stock, weight
                    )

                elif product_type == "2":
                    download_size = float(input("Download Size (MB): "))

                    if download_size < 0:
                        print("Download size cannot be negative.")
                        continue

                    new_product = DigitalProduct(
                        product_id, name, price, stock, download_size
                    )

                inventory.add_product(new_product)

            except ValueError:
                print("Invalid numeric input.")

        elif choice == "3":
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)

            if product is not None:
                product.display_information()

                try:
                    new_stock = int(input("New Stock Quantity: "))

                    if new_stock < 0:
                        print("Stock cannot be negative.")
                        continue

                    product.update_stock(new_stock)
                    print("Stock updated successfully!")

                except ValueError:
                    print("Invalid stock quantity.")
            else:
                print("Product not found.")

        elif choice == "4":
            product_id = input("Enter Product ID: ").strip()
            product = inventory.search_product(product_id)

            if product is not None:
                print("\nProduct Found:")
                product.display_information()
                print(product.get_fulfilment_info())

                if isinstance(product, PhysicalProduct):
                    print(
                        f"Shipping Cost: "
                        f"${product.calculate_shipping_cost():.2f}"
                    )
            else:
                print("Product not found.")

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            break

        else:
            print("Invalid option. Please enter 1 to 6.")


if __name__ == "__main__":
    main()
