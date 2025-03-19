import sys
import os
import unittest

# Ensure the project root directory is in the module search path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from find_min_max import find_min_max_even

class TestFindMinMaxEven(unittest.TestCase):
    def test_find_min_max_even(self):
        self.assertEqual(find_min_max_even([4, 2, 8, 6]), (2, 8))
        self.assertEqual(find_min_max_even([10]), (10, 10))

        with self.assertRaises(ValueError):
            find_min_max_even([])

if __name__ == "__main__":
    unittest.main()
