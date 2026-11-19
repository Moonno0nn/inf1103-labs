from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float, 
               stock_quantity: int, supplier: Supplier = None, **kwargs) -> Product:
        ptype = product_type.strip().lower()

        if ptype == "physical":
            weight = kwargs.get("weight", 0.0)
            return PhysicalProduct(product_id, name, price, stock_quantity, weight=weight, supplier=supplier)
        elif ptype == "digital":
            file_size = kwargs.get("file_size", 0.0)
            return DigitalProduct(product_id, name, price, stock_quantity, file_size=file_size, supplier=supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
