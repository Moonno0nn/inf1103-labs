
inventory = 0  # Initialize the inventory to zero
failed_entries = 0
delivery_processed = 0

INVENTORY_FILE = "inventory.txt"

#History Tracking
#Write Back
#load_inventory
#save_inventory

def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return 0, []
 
    if not lines:
        return 0, []
 
    total = int(lines[0])
    history = [int(value) for value in lines[1:] if value.strip() != ""]
    return total, history

def save_inventory(total, history):
    with open(INVENTORY_FILE, "w") as f:
        f.write(f"{total}\n")
        for value in history:
            f.write(f"{value}\n")

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


def generate_report(total_units, failed_attempts, history):
    print("\n------- Final Report -------")
    print(f"The total deliveries processed: {delivery_processed}")
    print(f"The final total units in inventory: {total_units}")
    print(f"The number of failed/rejected entries: {failed_attempts}")
    print(f"Transaction history (Order successfully saved to inventory.txt): {history}")

inventory, transaction_history = load_inventory()

while True:
    print("Current Orders:")
    print("1001, wireless Mouse, 2")
    print("1002, Keyboard, 1")
    print("1003, USB Cable, 3")    
    order = input("Enter Product Name: ")
    quantity = input("Enter Quantity: ")

    print("New Order Added:")
    print(f"1004,{order},{quantity}")
    print("Order successfully saved to orders.txt")

    stock = get_valid_input()


    if stock == "quit":
        save_inventory(inventory, transaction_history)
        generate_report(inventory, failed_entries, transaction_history)
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)
    transaction_history.append(stock)

    tax = calculate_tax(stock)

    delivery_processed += 1

    print(f"Current inventory: {inventory}")
    print(f"Tax for this delivery: {tax:.2f}")
