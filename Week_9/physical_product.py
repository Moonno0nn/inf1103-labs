from product import Product
from can_be_shipped import CanBeShipped
#1. init the Physical Products
#2. Get for weight
#3. display the information of the physical product
#4.Return a message for explaining physical shipping
# 5.Calculate shipping cost based on weight

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def __str__(self):
        return f"{super().__str__()}, Weight: {self.__weight} kg"

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product will be shipped to the customer. Weight: {} kg".format(self.__weight)

    def calculate_shipping_cost(self):
        shipping_cost = self.__weight * 5  # Assuming $5 per kg
        return shipping_cost