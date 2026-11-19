from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, file_size: float = 0.0, supplier: Supplier = None):
        super().__init__(product_id, name, price, stock, supplier)
        if file_size < 0:
            raise ValueError("File size cannot be negative.")
        self.__file_size = file_size

    def get_download_size(self):
        return self.__file_size

    def __str__(self):
        return f"{super().__str__()}, File Size: {self.__file_size} MB"

    def display_information(self):
        super().display_information()
        print(f"File Size: {self.__file_size} MB")

    def get_fulfilment_info(self):
        return "This product is a delivered digitally. File Size: {} MB".format(self.__file_size)
