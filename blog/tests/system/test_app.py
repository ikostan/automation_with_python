import unittest
import os
from unittest.mock import patch
from blog.app import App
from blog.blog import Blog
import blog.main as main
from blog.post import Post


class AppTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.dirname(__file__) + '\\' + os.path.basename(__file__) + "\n")

    def test_main_calls_print_blogs(self):
        with patch('blog.app.App.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                main.main()
                mocked_print_blogs.assert_called()

    def test_app_print_blogs_0_posts(self):
        app = App()
        blog = Blog("Blog", "First Last")
        app.add_blog('first blog', blog)
        expected = '- Blog by First Last (0 post)'
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(expected)

    def test_app_print_blogs_1_post(self):
        app = App()
        blog = Blog("Blog", "First Last")
        blog.create_post("Test post", "Test Content")
        app.add_blog('first blog', blog)
        expected = '- Blog by First Last (1 post)'
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
        title = "Post title"
        content = "Post content"
        post = Post(title, content)
        expected = '''
                    --- {0} ---
        
                    {1}
                
                    '''.format(' '.join([word.capitalize() for word in title.split(' ')]), content)
        with patch('builtins.print') as mocked_print:
            app = App()
            app.print_post(post)
            mocked_print.assert_called_with(expected)

    def test_ask_create_post(self):
        app = App()
        blog_name = "Blog Name"
        blog = Blog(blog_name, "First Last")
        app.blogs[blog_name] = blog
        expected = {
            'title': "Post Title",
            'content': "Post Content",
        }
        with patch('builtins.input') as mocked_input:
            # blog_name, post_title, post_content
            post_title = "Post Title"
            post_content = "Post Content"
            mocked_input.side_effect = (blog_name, post_title, post_content)
            app.ask_create_post()
            self.assertIsNotNone(app.blogs["Blog Name"].posts[0])
            self.assertDictEqual(expected, app.blogs["Blog Name"].posts[0].json())
            self.assertEqual(app.blogs["Blog Name"].posts[0].title, post_title)
            self.assertEqual(app.blogs["Blog Name"].posts[0].content, post_content)

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
            with patch('blog.app.App.ask_create_blog') as mocked_ask_create_blog:
                user_selection = 'c'
                blog_name = 'Blog Title'
                author_name = 'Author Name'
                mocked_input.side_effect = (user_selection, blog_name, author_name, 'q')
                main.main()
                mocked_ask_create_blog.assert_called()


if __name__ == '__main__':
    unittest.main()
