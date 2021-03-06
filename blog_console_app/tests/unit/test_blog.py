import unittest
import os
from blog_console_app.blog import Blog


class BlogTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.dirname(__file__) + '\\' + os.path.basename(__file__) + "\n")

    def setUp(self):
        self.title = 'Test'
        self.author = 'First Last'
        self.new_blog = Blog(self.title, self.author)

    def test_blog_title(self):
        self.assertEqual(self.title, self.new_blog.title)

    def test_blog_title_capitalized(self):
        title = 'test title'
        author = 'First Last'
        new_blog = Blog(title, author)
        expected_title = 'Test Title'
        self.assertEqual(expected_title, new_blog.title)

    def test_blog_author(self):
        self.assertEqual(self.author, self.new_blog.author)

    def test_blog_author_capitalized(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        expected = 'First Last'
        self.assertEqual(expected, new_blog.author)

    def test_initial_posts_length(self):
        expected_length = 0
        self.assertEqual(expected_length, len(self.new_blog.posts))

    def test_initial_posts_list(self):
        expected_list = []
        self.assertListEqual(expected_list, self.new_blog.posts)

    def test_multiple_posts_list(self):
        self.new_blog.posts = ['post #1', 'post #2']
        expected_list = ['post #1', 'post #2']
        self.assertListEqual(expected_list, self.new_blog.posts)

    def test_repr(self):
        expected = 'Test by First Last (0 post)'
        self.assertEqual(expected, self.new_blog.__repr__())

    def test_repr_multiple_posts(self):
        self.new_blog.posts = ['post #1', 'post #2']
        expected = 'Test by First Last (2 posts)'
        self.assertEqual(expected, self.new_blog.__repr__())


if __name__ == '__main__':
    unittest.main()
