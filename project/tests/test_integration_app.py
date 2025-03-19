import unittest
from unittest.mock import patch
from app import create_random_number_list
from find_min_max import find_min_max_even

class TestIntegration(unittest.TestCase):
    @patch("random.randint")
    def test_integration_even_major(self, mock_randint):
        """
        Test the integration when the list contains >= 50% even numbers.
        """
        # Mock random.randint to return a fixed list with more than 50% even numbers
        mock_randint.side_effect = [2, 4, 6, 8, 14] * 60  # 300 elements, all even
        result = create_random_number_list()
        self.assertIn("Even min number: 2", result)
        self.assertIn("Even max number: 14", result)

    @patch("random.randint")
    def test_integration_even_minor(self, mock_randint):
        """
        Test the integration when the list contains < 50% even numbers.
        """
        # Mock random.randint to return a fixed list with less than 50% even numbers
        mock_randint.side_effect = [1, 3, 5, 7, 9] * 180 + [2, 4, 6, 8, 10] * 120  # 40% even
        result = create_random_number_list()
        self.assertEqual(result, "Even numbers shoulbe equal major than 50%")

if __name__ == "__main__":
    unittest.main()