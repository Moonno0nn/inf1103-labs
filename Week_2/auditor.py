inventory = 0
failed_entires = 0

while True:
    stock = input("Enter stock quantity (or 'quit' to finish):")
    if stock.lower() == "quit":
        break
    if not stock.isdigit():
        print("Error: Invalid input. Please enter a positive whole number.")
        failed_entires += 1
        continue
    quantity = int(stock)

    if quantity < 0:
        print("Error: Negative stock quantities are not allowed.")
        failed_entries += 1
        continue
    
    inventory += quantity 
    print(f"Stock accepted. Current inventory:{inventory}")

    if inventory > 500:
        print("ALERT: OVERSTOCK! INVENTORY EXCEEDS 500 UNITS")
        break
print("\n -- Inventory Report----")
print(f"Total Units Processed: {inventory}")
print(f"Number of Failed/Rejected Entries:{failed_entires}")

####Week2##########