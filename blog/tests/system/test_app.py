import unittest
from unittest.mock import patch
from blog.app import App
from blog.blog import Blog
import blog.main as main


class AppTestCase(unittest.TestCase):

    def test_app_print_blogs(self):
        app = App()
        blog = Blog("Blog", "First Last")
        app.add_blog('first blog', blog)
        expected = '- Blog by First Last (0 post)'
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(expected)

    def test_main_calls_print_blogs(self):
        with patch('blog.app.App.print_blogs') as mocked_print_blogs:
            with patch('builtins.input') as moked_input:
                main.main()
                mocked_print_blogs.assert_called()

    def test_main_calls_menu(self):
        with patch('builtins.input') as mocked_input:
            main.main()
            mocked_input.assert_called()


if __name__ == '__main__':
    unittest.main()
