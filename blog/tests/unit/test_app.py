import unittest
from blog.app import App
from unittest.mock import patch


class MyTestCase(unittest.TestCase):

    def test_app_menu(self):
        app = App()
        expected = "Enter 'c' to create a blog, " \
                   "'l' to list blogs, " \
                   "'r' to read one, " \
                   "'p' to create a post, " \
                   "or 'q' to quit."

        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(expected)


if __name__ == '__main__':
    unittest.main()
