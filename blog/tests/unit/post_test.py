import unittest
from blog.post import Post


class PostTest(unittest.TestCase):
    def test_create_post(self):
        title = 'Test'
        content = 'Test Content'
        new_post = Post(title, content)
        self.assertEqual(title, new_post.title)
        self.assertEqual(content, new_post.content)


if __name__ == '__main__':
    unittest.main()
