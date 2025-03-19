import unittest
from unittest.mock import patch
from find_min_max import find_min_max_even
from app import create_random_number_list

class TestCreateRandomNumberList(unittest.TestCase):
    @patch('random.randint')
    def test_even_numbers_above_50_percent(self, mock_randint):
        """Test when even numbers are >= 50%"""
        mock_randint.side_effect = [2, 4, 6, 8, 10] * 60  # 300 numbers, all even

        result = create_random_number_list()

        # Since we control the even numbers, we can predict min and max
        self.assertEqual(result, ("Even min number: 2", "Even max number: 10"))

    @patch('random.randint')
    def test_even_numbers_below_50_percent(self, mock_randint):
        """Test when even numbers are < 50%"""
        mock_randint.side_effect = [1, 3, 5, 7, 9] * 60  # 300 numbers, all odd

        result = create_random_number_list()

        self.assertEqual(result, "Even numbers shoulbe equal major than 50%")

if __name__ == "__main__":
    unittest.main()
