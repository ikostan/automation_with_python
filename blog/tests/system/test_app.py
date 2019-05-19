import unittest
from unittest.mock import patch
from blog.app import App
from blog.blog import Blog
import blog.main as main
from blog.post import Post


class AppTestCase(unittest.TestCase):

    def test_main_calls_print_blogs(self):
        with patch('blog.app.App.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                main.main()
                mocked_print_blogs.assert_called()

    def test_app_print_blogs(self):
        app = App()
        blog = Blog("Blog", "First Last")
        app.add_blog('first blog', blog)
        expected = '- Blog by First Last (0 post)'
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(expected)

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            app = App()
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        app = App()
        blog = Blog("Test", "First Last")
        app.add_blog("Test", blog)
        with patch('builtins.input', return_value="Test"):
            with patch('blog.app.App.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        app = App()
        blog = Blog("Test", "First Last")
        blog.create_post("Test post", "Test Content")
        app.add_blog("Test", blog)
        with patch('blog.app.App.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post("Post title", "Post content")
        expected = '''
                    --- Post Title ---
        
                    Post content
                
                    '''
        with patch('builtins.print') as mocked_print:
            app = App()
            app.print_post(post)
            mocked_print.assert_called_with(expected)


if __name__ == '__main__':
    unittest.main()
