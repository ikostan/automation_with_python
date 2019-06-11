from starter_code_section_7.tests.base_test import BaseTest
from starter_code_section_7.models.store import StoreModel
from starter_code_section_7.models.user import UserModel
from starter_code_section_7.models.item import ItemModel
import json


class ItemSystemTest(BaseTest):

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                item_name = 'test item'
                resp = client.get('item/{}'.format(item_name))

                # Authorisation error code
                self.assertEqual(401, resp.status_code)
                # Authorisation error message
                self.assertDictEqual({'message': 'Could not authorize. Invalid Authorization header!'},
                                     json.loads(resp.data))

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                # create a user
                user_name = 'user'
                user_pswd = '1234'
                UserModel(user_name, user_pswd).save_to_db()

                # authorisation
                auth_request = client.post('/auth',
                                           data=json.dumps({'username': user_name,
                                                            'password': user_pswd}),
                                           headers={'Content-Type': 'application/json'})

                # authorisation token
                jwt_token = json.loads(auth_request.data)["access_token"]

                header = {'Authorization': 'JWT ' + jwt_token}

                item_name = 'test item'
                resp = client.get('item/{}'.format(item_name), headers=header)

                # Item not found error code
                self.assertEqual(404, resp.status_code)
                # Item not found error message
                self.assertDictEqual({'message': 'Item not found'},
                                     json.loads(resp.data))

    def test_get_item(self):
        pass

    def test_delete_item(self):
        pass

    def test_create_item(self):
        pass

    def test_duplicate_item(self):
        pass

    def test_update_item(self):
        pass

    def test_item_list(self):
        pass




