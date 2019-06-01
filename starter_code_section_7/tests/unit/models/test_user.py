from starter_code_section_7.models.user import UserModel
from starter_code_section_7.tests.unit.unit_base_test import BaseUnitTestCase


class UserUnitTest(BaseUnitTestCase):
    def test_init(self):
        user_name = 'uname'
        password = 'password'
        user = UserModel(user_name, password)

        self.assertEqual(user_name, user.username)
        self.assertEqual(password, user.password)

