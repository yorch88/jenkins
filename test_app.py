import unittest
from app import sum, sub, mul, div

class TestMathOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(10, 5), 15)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(mul(10, 5), 50)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(-1, -1), 1)

    def test_div(self):
        self.assertEqual(div(10, 5), 4)
        self.assertEqual(div(-1, 1), -1)
        self.assertEqual(div(-1, -1), 1)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

if __name__ == "__main__":
    unittest.main()