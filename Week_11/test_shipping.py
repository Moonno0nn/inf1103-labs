from physical_product import PhysicalProduct

product1 = PhysicalProduct("P001", "Laptop", 999.99, 10, 2.5)
product2 = PhysicalProduct("P002", "Smartphone", 499.99, 20, 0.3)

print(f"Laptop Shipping Cost: ${product1.calculate_shipping_cost():.2f}")
print(f"Smartphone Shipping Cost: ${product2.calculate_shipping_cost():.2f}")