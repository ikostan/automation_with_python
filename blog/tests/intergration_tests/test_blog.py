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

    def test_json(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        new_blog.create_post('Test post', 'Test content')
        expected = {'title': title,
                    'author': 'First Last',
                    'posts': [{'title': 'Test Post',
                               'content': 'Test content'}]}
        # Tests
        self.assertDictEqual(expected, new_blog.json())

    def test_json_no_posts(self):
        title = 'Test'
        author = 'first last'
        new_blog = Blog(title, author)
        expected = {'title': title,
                    'author': 'First Last',
                    'posts': []}
        # Tests
        self.assertDictEqual(expected, new_blog.json())



if __name__ == '__main__':
    unittest.main()
