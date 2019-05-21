import unittest
from flask_app.app import app


class HomeTestCase(unittest.TestCase):
    def test_home(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
