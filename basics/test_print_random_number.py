# mock
# Mock, MagicMock
# patch
# ExitStack
import unittest
import print_random_number
from unittest.mock import patch


class TestPrintRandomNumber(unittest.TestCase):
    @patch('print_random_number.random.randint')
    def test_function_should_call_randint_with_1_and_10(self, mock):
        print_random_number.print_random_number()
        mock.assert_called_once_with(1, 10)

    @patch('print_random_number.random.randint')
    def test_get_3_should_return_three(self, mock):
        mock.return_value = 3
        result = print_random_number.print_random_number()
        self.assertEqual(result, 'three')

    @patch('print_random_number.random.randint')
    def test_get_5_should_return_five(self, mock):
        mock.return_value = 5
        result = print_random_number.print_random_number()
        self.assertEqual(result, 'five')

# Comment this when we run pytest
# unittest.main()