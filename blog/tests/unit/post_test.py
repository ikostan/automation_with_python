import unittest
from blog.post import Post


class PostTest(unittest.TestCase):

    def test_assert_title(self):
        title = 'Test'
        content = 'Test Content'
        new_post = Post(title, content)
        self.assertEqual(title, new_post.title)

    def test_assert_title_capitalized(self):
        title = 'test'
        content = 'Test Content'
        new_post = Post(title, content)
        self.assertEqual(title.capitalize(), new_post.title)

    def test_assert_content(self):
        title = 'Test'
        content = 'Test Content'
        new_post = Post(title, content)
        self.assertEqual(content, new_post.content)

    def test_assert_json(self):
        title = 'Test'
        content = 'Test Content'
        new_post = Post(title, content)
        expected = {
                    'title': title,
                    'content': content,
                    }
        self.assertDictEqual(expected, new_post.json())

    def test_assert_json_title_capitalized(self):
        title = 'test'
        content = 'Test Content'
        new_post = Post(title, content)
        expected = {
                    'title': title.capitalize(),
                    'content': content,
                    }
        self.assertDictEqual(expected, new_post.json())


if __name__ == '__main__':
    unittest.main()
