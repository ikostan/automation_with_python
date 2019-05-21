import unittest
import os
from blog_console_app.post import Post


class PostTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.dirname(__file__) + '\\' + os.path.basename(__file__) + "\n")

    def setUp(self):
        self.title = 'Test'
        self.content = 'Test Content'
        self.new_post = Post(self.title, self.content)

    def test_assert_title(self):
        self.assertEqual(self.title, self.new_post.title)

    def test_assert_title_capitalized(self):
        title = 'test title'
        content = 'Test Content'
        new_post = Post(title, content)
        expected_title = 'Test Title'
        self.assertEqual(expected_title, new_post.title)

    def test_assert_content(self):
        self.assertEqual(self.content, self.new_post.content)

    def test_assert_json(self):
        expected = {
                    'title': self.title,
                    'content': self.content,
                    }
        self.assertDictEqual(expected, self.new_post.json())

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
