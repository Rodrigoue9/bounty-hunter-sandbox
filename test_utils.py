import unittest
from utils import calculate_discount

class TestUtils(unittest.TestCase):
    def test_calculate_discount_zero(self):
        self.assertEqual(calculate_discount(100.0, 0.0), 100.0)

    def test_calculate_discount_normal(self):
        self.assertEqual(calculate_discount(50.0, 10.0), 45.0)

    def test_calculate_discount_full(self):
        self.assertEqual(calculate_discount(200.0, 100.0), 0.0)

if __name__ == "__main__":
    unittest.main()
