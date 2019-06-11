from starter_code_section_7.tests.base_test import BaseTest
from starter_code_section_7.models.store import StoreModel
from starter_code_section_7.models.user import UserModel
from starter_code_section_7.models.item import ItemModel
import json


class ItemSystemTest(BaseTest):

    def setUp(self):
        super(ItemSystemTest, self).setUp()
        with self.app() as client:
            with self.app_context():

                # item data
                self.item_name = 'ChromeBook'
                self.item_price = 199.99
                self.store_id = 1

                # create a store
                store_name = 'Electronics'
                StoreModel(store_name).save_to_db()

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

                self.header = {'Authorization': 'JWT ' + jwt_token}

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('item/{}'.format(self.item_name))

                # Authorisation error code
                self.assertEqual(401, resp.status_code)
                # Authorisation error message
                self.assertDictEqual({'message': 'Could not authorize. Invalid Authorization header!'},
                                     json.loads(resp.data))

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('item/{}'.format(self.item_name), headers=self.header)

                # Item not found error code
                self.assertEqual(404, resp.status_code)
                # Item not found error message
                self.assertDictEqual({'message': 'Item not found'},
                                     json.loads(resp.data))

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                # create an item
                ItemModel(self.item_name, self.item_price, self.store_id).save_to_db()

                resp = client.get('item/{}'.format(self.item_name), headers=self.header)

                # Item response code
                self.assertEqual(200, resp.status_code)
                # Item response message
                self.assertDictEqual({'name': self.item_name, 'price': self.item_price},
                                     json.loads(resp.data))

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                # create an item
                ItemModel(self.item_name, self.item_price, self.store_id).save_to_db()
                self.assertIsNotNone(ItemModel.find_by_name(self.item_name))

                resp = client.delete('item/{}'.format(self.item_name))

                # response code
                self.assertEqual(200, resp.status_code)
                # response message
                self.assertDictEqual({'message': 'Item deleted'},
                                     json.loads(resp.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                resp = client.post('/item/{0}'.format(self.item_name),
                                   data={'price': self.item_price,
                                         'store_id': self.store_id})

                # response message
                self.assertDictEqual({'name': self.item_name, 'price': self.item_price},
                                     json.loads(resp.data))
                # response code
                self.assertEqual(201, resp.status_code)

    def test_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                client.post('/item/{0}'.format(self.item_name),
                            data={'price': self.item_price,
                                  'store_id': self.store_id})

                # duplicate
                resp = client.post('/item/{0}'.format(self.item_name),
                                   data={'price': self.item_price,
                                         'store_id': self.store_id})

                # response error message
                self.assertDictEqual({'message':
                                      "An item with name '{0}' already exists.".format(
                                          self.item_name)},
                                     json.loads(resp.data))
                # response error code
                self.assertEqual(400, resp.status_code)

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                client.put('/item/{0}'.format(self.item_name),
                           data={'price': self.item_price,
                                 'store_id': self.store_id})
                # test DB
                self.assertEqual(ItemModel.find_by_name(self.item_name).price, self.item_price)

                # update
                new_price = 299.00
                resp = client.put('/item/{0}'.format(self.item_name),
                                  data={'price': new_price,
                                        'store_id': self.store_id})

                # response message
                self.assertDictEqual({'name': self.item_name, 'price': new_price},
                                     json.loads(resp.data))
                # response code
                self.assertEqual(200, resp.status_code)

                # test DB
                self.assertEqual(ItemModel.find_by_name(self.item_name).price, new_price)

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                resp = client.put('/item/{0}'.format(self.item_name),
                                  data={'price': self.item_price,
                                        'store_id': self.store_id})

                # response message
                self.assertDictEqual({'name': self.item_name, 'price': self.item_price},
                                     json.loads(resp.data))
                # response code
                self.assertEqual(200, resp.status_code)

                # test DB
                self.assertEqual(ItemModel.find_by_name(self.item_name).price, self.item_price)

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                # create new items
                client.put('/item/{0}'.format(self.item_name),
                           data={'price': self.item_price,
                                 'store_id': self.store_id})

                item_name_2 = "Flush Memory"
                item_price_2 = 99.99
                client.put('/item/{0}'.format(item_name_2),
                           data={'price': item_price_2,
                                 'store_id': self.store_id})

                item_name_3 = "Keyboard"
                item_price_3 = 125.88
                client.put('/item/{0}'.format(item_name_3),
                           data={'price': item_price_3,
                                 'store_id': self.store_id})

                resp = client.get('/items')

                # response code
                self.assertEqual(200, resp.status_code)

                # response message
                self.assertDictEqual({'items': [{'name': self.item_name, 'price': self.item_price},
                                                {'name': item_name_2, 'price': item_price_2},
                                                {'name': item_name_3, 'price': item_price_3}]},
                                     json.loads(resp.data))

