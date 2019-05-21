import unittest
import os
from flask_app.app import app


class HomeTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.dirname(__file__) + '\\' + os.path.basename(__file__) + "\n")

    def test_home(self):
        # make a request for the app
        with app.test_client() as client:
            #  response variable
            resp = client.get('/')
            # test response status code, should be 200
            self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()
