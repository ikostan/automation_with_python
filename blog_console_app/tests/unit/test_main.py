import unittest
import os
from unittest.mock import patch
import blog_console_app.main as main


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.dirname(__file__) + '\\' + os.path.basename(__file__) + "\n")

    #  TODO: create a setUp method

    def test_app_menu_prints_prompt(self):
        expected = "Enter 'c' to create a blog_console_app, " \
                   "'l' to list blogs, " \
                   "'r' to read one, " \
                   "'p' to create a post, " \
                   "or 'q' to quit."

        with patch('builtins.input', return_value='q') as mocked_input:
            main.main()
            mocked_input.assert_called_with(expected)


if __name__ == '__main__':
    unittest.main()
