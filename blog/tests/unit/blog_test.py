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


if __name__ == '__main__':
    unittest.main()
