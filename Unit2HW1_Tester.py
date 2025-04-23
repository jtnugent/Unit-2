import unittest
import unittest.mock
from Unit2HW2 import Restaurant,User

class TestRestaurant(unittest.TestCase):

    def setUp(self):
        """Set up a restaurant instance for testing."""
        self.restaurant = Restaurant("Bob's Burgers", "Burgers")

    def test_attributes(self):
        """Test restaurant name and cuisine type attributes."""
        self.assertEqual(self.restaurant.restaurant_name, "Bob's Burgers")
        self.assertEqual(self.restaurant.cuisine_type, "Burgers")

    def test_describe_restaurant(self):
        """Test describe_restaurant method (output test, requires patching print)."""
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.restaurant.describe_restaurant()
            mocked_print.assert_called_with("Restaurant name: Bob's Burgers\nRestaurant cuisine: Burgers")

    def test_open_restaurant(self):
        """Test open_restaurant method."""
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.restaurant.open_restaurant()
            mocked_print.assert_called_with("Bob's Burgers is open")

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up a user instance for testing."""
        self.user = User("Jimmy", "Pesto")

    def test_attributes(self):
        """Test user first and last name attributes."""
        self.assertEqual(self.user.first_name, "Jimmy")
        self.assertEqual(self.user.last_name, "Pesto")

    def test_describe_user(self):
        """Test describe_user method."""
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.user.describe_user()
            mocked_print.assert_called_with("First Name: Jimmy\nLast Name: Pesto")

    def test_greet_user(self):
        """Test greet_user method."""
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.user.greet_user()
            mocked_print.assert_called_with("Welcome Jimmy!")

if __name__ == '__main__':
    unittest.main()