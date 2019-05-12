import unittest
from unittest.mock import patch
from blog.app import App
from blog.blog import Blog


class AppTestCase(unittest.TestCase):

    def test_app_print_blogs(self):
        app = App()
        blog = Blog("Blog", "First Last")
        app.add_blog('first blog', blog)
        expected = "- Blog by First Last (0 post)"
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(expected)


if __name__ == '__main__':
    unittest.main()
