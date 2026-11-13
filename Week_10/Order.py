
from Orderline import Orderline
from product import Product

class Order:
    def __init__(self, order_id:str):
        #1. Order_id: a unique identifier for the order
        #2. Order_lines: a collection of Orderline objects.
        self.order_id: str = order_id
        self.order_lines: list[Orderline] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = Orderline(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return total
    
    def remove_order_line(self, index: int) -> None:
      if 0 <= index < len(self.order_lines):
          self.order_lines.pop(index)