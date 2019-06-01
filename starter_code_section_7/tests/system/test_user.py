from starter_code_section_7.tests.base_test import BaseTest
from starter_code_section_7.models.user import UserModel
import json


class UserSystemTest(BaseTest):
    # Test User registration:
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                username = 'uname'
                request = client.post('/register',
                                      data={'username': username,
                                            'password': 'password'})

                # Assert response
                self.assertEqual(request.status_code, 201)
                self.assertDictEqual(json.loads(request.data),
                                     {'message': 'User created successfully.'})

                # Assert user in DB
                self.assertIsNotNone(UserModel.find_by_username(username))
                self.assertIsNotNone(UserModel.find_by_id(1))

    def test_register_and_login(self):
        pass

    def test_register_duplicate_user(self):
        pass

