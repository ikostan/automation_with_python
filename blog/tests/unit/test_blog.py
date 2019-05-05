import unittest
from blog.blog import Blog


class BlogTestCase(unittest.TestCase):
    def test_blog_title(self):
        title = 'Test'
        author = 'First Last'
        new_blog = Blog(title, author)
        self.assertEqual(title, new_blog.title)

    def test_blog_title_capitalized(self):
        title = 'test'
        author = 'First Last'
        new_blog = Blog(title, author)
        self.assertEqual(title.capitalize(), new_blog.title)

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


if __name__ == '__main__':
    unittest.main()
