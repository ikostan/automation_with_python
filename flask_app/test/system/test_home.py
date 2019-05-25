from flask_app.test.system.base_test import BaseTestCase
import os
import json


class HomeTestCase(BaseTestCase):

    print("Running unit tests from: " + os.path.dirname(__file__) + '\\' + os.path.basename(__file__) + "\n")

    def test_home_response_code(self):
        # make a request for the app with a test client
        with self.app as client:
            #  response variable
            resp = client.get('/')
            # test response status code, should be 200
            self.assertEqual(resp.status_code, 200)

    def test_home_json_data(self):
        # make a request for the app with a test client
        with self.app as client:
            #  response variable
            resp = client.get('/')
            # verify json data by loading string and converting it into json/dictionary
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello, world!'})

