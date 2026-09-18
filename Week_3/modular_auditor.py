
inventory = 0  # Initialize the inventory to zero
failed_entries = 0
delivery_processed = 0


def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def get_valid_input():
    stock = input("Enter stock quantity (Enter 'quit' to finish): ")

    if stock.lower() == "quit":
        return "quit"

    if not stock.isdigit():
        print("Error: Invalid input.")
        return None

    print(f"Current stock: {stock}")
    return int(stock)


def calculate_tax(amount):
    tax = amount * 0.10
    return tax


def generate_report(total_units, failed_attempts):
    print("\n------- Final Report -------")
    print(f"The total deliveries processed: {delivery_processed}")
    print(f"The final total units in inventory: {total_units}")
    print(f"The number of failed/rejected entries: {failed_attempts}")


while True:
    stock = get_valid_input()

    if stock == "quit":
        generate_report(inventory, failed_entries)
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)

    tax = calculate_tax(stock)

    delivery_processed += 1

    print(f"Current inventory: {inventory}")
    print(f"Tax for this delivery: {tax:.2f}")
