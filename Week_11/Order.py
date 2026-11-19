from discount_strategy import DiscountStrategy, NoDiscount
from Orderline import Orderline
from product import Product

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None):
        self.order_id: str = order_id
        self.order_lines: list[Orderline] = []
        self.discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def set_discount(self, discount: DiscountStrategy) -> None:
        """Allow switching the discount strategy at runtime."""
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = Orderline(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = sum(order_line.calculate_subtotal() for order_line in self.order_lines)
        return self.discount.apply(total)
    
    def remove_order_line(self, index: int) -> None:
        if 0 <= index < len(self.order_lines):
            self.order_lines.pop(index)
