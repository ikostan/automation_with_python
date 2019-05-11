import unittest
from blog.blog import Blog



class MyTestCase(unittest.TestCase):
    def test_create_post_in_blog(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        new_blog.create_post('Test post', 'Test content')
        # Tests
        self.assertEqual(1, len(new_blog.posts))
        self.assertEqual('Test Post', new_blog.posts[0].title)
        self.assertEqual('Test content', new_blog.posts[0].content)


if __name__ == '__main__':
    unittest.main()
