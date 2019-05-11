import unittest
from blog.blog import Blog


class BlogTestCase(unittest.TestCase):

    def test_blog_title(self):
        title = 'Test'
        author = 'First Last'
        new_blog = Blog(title, author)
        self.assertEqual(title, new_blog.title)

    def test_blog_title_capitalized(self):
        title = 'test title'
        author = 'First Last'
        new_blog = Blog(title, author)
        expected_title = 'Test Title'
        self.assertEqual(expected_title, new_blog.title)

    def test_blog_author(self):
        title = 'Test'
        author = 'First Last'
        new_blog = Blog(title, author)
        self.assertEqual(author, new_blog.author)

    def test_blog_author_capitalized(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        expected = 'First Last'
        self.assertEqual(expected, new_blog.author)

    def test_initial_posts_length(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        expected_length = 0
        self.assertEqual(expected_length, len(new_blog.posts))

    def test_initial_posts_list(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        expected_list = []
        self.assertListEqual(expected_list, new_blog.posts)

    def test_multiple_posts_list(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        new_blog.posts = ['post #1', 'post #2']
        expected_list = ['post #1', 'post #2']
        self.assertListEqual(expected_list, new_blog.posts)

    def test_repr(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        expected = 'Test by First Last (0 post)'
        self.assertEqual(expected, new_blog.__repr__())

    def test_repr_multiple_posts(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        new_blog.posts = ['post #1', 'post #2']
        expected = 'Test by First Last (2 posts)'
        self.assertEqual(expected, new_blog.__repr__())

    def test_json(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
