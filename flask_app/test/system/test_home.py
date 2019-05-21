import unittest
import os
import json
from flask_app.app import app


class HomeTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.dirname(__file__) + '\\' + os.path.basename(__file__) + "\n")

    def test_home(self):
        # make a request for the app with a test client
        with app.test_client() as client:
            #  response variable
            resp = client.get('/')
            # test response status code, should be 200
            self.assertEqual(resp.status_code, 200)
            # verify json data by loading string and converting it into json/dictionary
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, world!'})


if __name__ == '__main__':
    unittest.main()
