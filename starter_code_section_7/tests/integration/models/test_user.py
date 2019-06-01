from starter_code_section_7.models.user import UserModel
from starter_code_section_7.tests.integration.integration_base_test import BaseTest


class UserTestCase(BaseTest):
    def test_crud(self):
        with self.app_context():
            user_name = 'uname'
            password = 'password'
            user = UserModel(user_name, password)

            self.assertIsNone(UserModel.find_by_username(user_name))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()
            self.assertIsNotNone(UserModel.find_by_username(user_name))
            self.assertIsNotNone(UserModel.find_by_id(1))


