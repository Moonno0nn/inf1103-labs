class Inventory:
    def __init__(self):
        self._products = []

    def get_products(self):
        return self._products.copy()

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print("Error: A product with this ID already exists.")
            return
        self._products.append(product)
        print("Product added successfully!")

    def search_product(self, product_id):
        for product in self._products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 35)
        if not self._products:
            print("No products available.")
        else:
            for product in self._products:
                product.display_information()
                print("-" * 35)
