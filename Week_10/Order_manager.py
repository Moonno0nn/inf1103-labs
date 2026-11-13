
from Order import Order
from product import Product
from Orderline import Orderline

def create_order(inventory):
    print("\n========== CREATE ORDER ==========")

    order_id = input("Enter Order ID: ").strip()

    order = Order(order_id)

    while True:
        product_id = input("\nEnter Product ID: ").strip()

        product = inventory.search_product(product_id)

        if product is None:
            print("Product not found!")
            continue

        product.display_information()

        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            if quantity > product.stock:
                print("Insufficient stock!")
                print(f"Available stock: {product.stock}")
                continue

            # Add product to Order
            order.add_order_line(product, quantity)

            print("Product added to order successfully!")

        except ValueError:
            print("Invalid quantity!")
            continue

        another = input(
            "\nAdd another product? (y/n): "
        ).strip().lower()

        if another != "y":
            break

    # Check whether order contains products
    if len(order.order_lines) == 0:
        print("No products added. Order cancelled.")
        return

    # Display order summary
    print("\n========== ORDER SUMMARY ==========")
    print(f"Order ID: {order.order_id}")

    for index, line in enumerate(order.order_lines, start=1):
        print(f"\nProduct {index}:")
        print(f"Product Name: {line.product.name}")
        print(f"Quantity: {line.quantity}")
        print(
            f"Subtotal: ${line.calculate_subtotal():.2f}"
        )

    print("-----------------------------------")
    print(f"Grand Total: ${order.calculate_total():.2f}")

    # Confirm order
    confirm = input(
        "\nConfirm Order? (y/n): "
    ).strip().lower()

    if confirm == "y":

        # Update product stock
        for line in order.order_lines:
            product = line.product
            new_stock = product.stock - line.quantity

            product.update_stock(new_stock)

        print("\nOrder created successfully!")
        print("Inventory stock updated.")

    else:
        print("\nOrder cancelled.")
