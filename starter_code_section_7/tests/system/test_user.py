from starter_code_section_7.tests.base_test import BaseTest
from starter_code_section_7.models.user import UserModel
import json


class UserSystemTest(BaseTest):
    # Test User registration:
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                username = 'uname'
                response = client.post('/register',
                                      data={'username': username,
                                            'password': 'password'})

                # Assert response
                self.assertEqual(response.status_code, 201)
                self.assertDictEqual(json.loads(response.data),
                                     {'message': 'User created successfully.'})

                # Assert user in DB
                self.assertIsNotNone(UserModel.find_by_username(username))
                self.assertIsNotNone(UserModel.find_by_id(1))

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                username = 'uname'
                password = 'password'
                client.post('/register',
                            data={'username': username,
                                  'password': password})

                auth_response = client.post('/auth',
                                           data=json.dumps({'username': username,
                                                            'password': password}),
                                           headers={'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_response.data).keys())  # 'access_token'

    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                username = 'uname'
                password = 'password'
                client.post('/register',
                            data={'username': username,
                                  'password': password})
                response = client.post('/register',
                                       data={'username': username,
                                             'password': password})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual(json.loads(response.data),
                                     {'message': 'A user with that username already exists.'})

