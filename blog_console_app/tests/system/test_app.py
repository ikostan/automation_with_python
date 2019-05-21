import unittest
import os
from unittest.mock import patch
from blog_console_app.app import App
from blog_console_app.blog import Blog
import blog_console_app.main as main
from blog_console_app.post import Post


class AppTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.dirname(__file__) + '\\' + os.path.basename(__file__) + "\n")

    def setUp(self) -> None:
        self.bloger_name = 'First Last'
        self.app = App()
        self.blog_name = "Blog Name"
        self.blog = Blog(self.blog_name, self.bloger_name)
        self.app.add_blog(self.blog_name, self.blog)

    def test_main_calls_print_blogs(self):
        with patch('blog_console_app.app.App.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                main.main()
                mocked_print_blogs.assert_called()

    def test_app_print_blogs_0_posts(self):
        expected = '- {0} by {1} (0 post)'.format(self.blog_name, self.bloger_name)
        with patch('builtins.print') as mocked_print:
            self.app.print_blogs()
            mocked_print.assert_called_with(expected)

    def test_app_print_blogs_1_post(self):
        self.blog.create_post("Test post", "Test Content")
        expected = '- {0} by {1} (1 post)'.format(self.blog_name, self.bloger_name)
        with patch('builtins.print') as mocked_print:
            self.app.print_blogs()
            mocked_print.assert_called_with(expected)

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            self.app.ask_create_blog()
            self.assertIsNotNone(self.app.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value=self.blog_name):
            with patch('blog_console_app.app.App.print_posts') as mocked_print_posts:
                self.app.ask_read_blog()
                mocked_print_posts.assert_called_with(self.blog)

    def test_print_posts(self):
        self.blog.create_post("Test post", "Test Content")
        with patch('blog_console_app.app.App.print_post') as mocked_print_post:
            self.app.print_posts(self.blog)
            mocked_print_post.assert_called_with(self.blog.posts[0])

    def test_print_post(self):
        title = "Post title"
        content = "Post content"
        post = Post(title, content)
        expected = '''
                    --- {0} ---
        
                    {1}
                
                    '''.format(' '.join([word.capitalize() for word in title.split(' ')]), content)
        with patch('builtins.print') as mocked_print:
            self.app.print_post(post)
            mocked_print.assert_called_with(expected)

    def test_ask_create_post(self):
        expected = {
            'title': "Post Title",
            'content': "Post Content",
        }
        with patch('builtins.input') as mocked_input:
            # blog_name, post_title, post_content
            post_title = "Post Title"
            post_content = "Post Content"
            mocked_input.side_effect = (self.blog_name, post_title, post_content)
            self.app.ask_create_post()
            self.assertIsNotNone(self.app.blogs["Blog Name"].posts[0])
            self.assertDictEqual(expected, self.app.blogs["Blog Name"].posts[0].json())
            self.assertEqual(self.app.blogs["Blog Name"].posts[0].title, post_title)
            self.assertEqual(self.app.blogs["Blog Name"].posts[0].content, post_content)

    def test_menu_create_blog(self):
        with patch('builtins.input') as mocked_input:
            user_selection = 'c'
            blog_name = 'Blog Title'
            author_name = 'Author Name'
            mocked_input.side_effect = (user_selection, blog_name, author_name, 'q')
            main.main()
            self.assertIsNotNone(main.app.blogs[blog_name])
            self.assertEqual(main.app.blogs[blog_name].author, author_name)
            self.assertEqual(main.app.blogs[blog_name].title, blog_name)

    def test_menu_calls_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('blog_console_app.app.App.ask_create_blog') as mocked_ask_create_blog:
                user_selection = 'c'
                mocked_input.side_effect = (user_selection, 'q')
                main.main()
                mocked_ask_create_blog.assert_called()

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('blog_console_app.app.App.print_blogs') as mocked_print_blogs:
                user_selection = 'l'
                mocked_input.side_effect = (user_selection, 'q')
                main.main()
                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_read_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('blog_console_app.app.App.ask_read_blog') as mocked_ask_read_blog:
                user_selection = 'r'
                mocked_input.side_effect = (user_selection, 'q')
                main.main()
                mocked_ask_read_blog.assert_called()

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('blog_console_app.app.App.ask_create_post') as mocked_ask_create_post:
                user_selection = 'p'
                mocked_input.side_effect = (user_selection, 'q')
                main.main()
                mocked_ask_create_post.assert_called()


if __name__ == '__main__':
    unittest.main()
