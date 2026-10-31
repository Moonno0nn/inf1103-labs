## Manager 1 product

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self._product_id

    def __str__(self):
        return f"ID: {self._product_id}, Name: {self._name}, Price: ${self._price:.2f}, Stock: {self._stock}"

    def update_stock(self, quantity):
        """Updates the stock quantity of the product."""
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")