import unittest
from flask_app.app import app


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        #  specify testing mode
        app.testing = True
        #  run test client
        self.app = app.test_client()


if __name__ == '__main__':
    unittest.main()
