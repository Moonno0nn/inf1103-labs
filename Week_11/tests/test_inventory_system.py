import sys
import os

# Ensure the parent directory (Week_11) is on Python's search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount
from Order import Order
from Orderline import Orderline
from inventory_manager import Inventory
from supplier import Supplier
from file_manager import load_products


class TestInventorySystem(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S01", "Supplier Co", "supp@test.com")
        self.product1 = ProductFactory.create("physical", "P01", "Item A", 50.0, 10, self.supplier)
        self.product2 = ProductFactory.create("digital", "D01", "Item B", 100.0, 5, self.supplier)

    # 1. Test Strategy Pattern
    def test_discount_strategies(self):
        order = Order("ORD1")
        order.add_order_line(self.product1, 2)  # 2 * 50 = 100
        order.add_order_line(self.product2, 1)  # 1 * 100 = 100 -> Total 200

        # No discount
        self.assertEqual(order.calculate_total(), 200.0)

        # Percentage discount 10%
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 180.0)

        # Bulk discount: 20 off over 150
        order.set_discount(BulkDiscount(150, 20))
        self.assertEqual(order.calculate_total(), 180.0)

        # Bulk discount below threshold
        order.set_discount(BulkDiscount(300, 50))
        self.assertEqual(order.calculate_total(), 200.0)

        # Student discount: 5% off
        order.set_discount(StudentDiscount(5))
        self.assertEqual(order.calculate_total(), 190.0)

    # 2. Test Factory Pattern
    def test_factory_creation(self):
        p = ProductFactory.create("physical", "P10", "Desk", 80.0, 4, self.supplier)
        self.assertIsInstance(p, PhysicalProduct)

        d = ProductFactory.create("digital", "D10", "EBook", 15.0, 20, self.supplier)
        self.assertIsInstance(d, DigitalProduct)

        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S10", "Repair", 30.0, 1, self.supplier)

    # 3. Test Validation
    def test_validation_rules(self):
        # Price <= 0
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P99", "Bad Price", -5.0, 10, self.supplier)

        # Stock < 0
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P99", "Bad Stock", 20.0, -1, self.supplier)

        # OrderLine quantity <= 0
        with self.assertRaises(ValueError):
            Orderline(self.product1, 0)

    # 4. Test File Loader with try/except
    def test_load_products_missing_file(self):
        inv = Inventory()
        # Should not crash on missing file
        load_products("non_existent_file.csv", inv, self.supplier)
        self.assertEqual(len(inv.get_products()), 0)

    def test_load_products_from_csv(self):
        inv = Inventory()
        csv_path = os.path.join(os.path.dirname(__file__), "..", "products.csv")
        if os.path.exists(csv_path):
            load_products(csv_path, inv, self.supplier)
            # products.csv has 5 rows: 3 valid (P001, D001, P003) and 2 invalid (service, abc price)
            self.assertEqual(len(inv.get_products()), 3)


if __name__ == "__main__":
    unittest.main()
