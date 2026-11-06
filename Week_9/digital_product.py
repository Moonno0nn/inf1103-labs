from product import Product

#1. init the Digital Products
#2. Get for download size
#3. display the information of the digital product
#4. Return a message for explaining digital delivery

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, file_size):
        super().__init__(product_id, name, price, stock)
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