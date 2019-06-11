from starter_code_section_7.tests.base_test import BaseTest
from starter_code_section_7.models.store import StoreModel
from starter_code_section_7.models.item import ItemModel

import json


class StoreSystemTest(BaseTest):

    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                response = client.post('/store/{0}'.format(store_name))
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name(store_name))
                self.assertDictEqual({'name': store_name, 'items': []}, json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                client.post('/store/{0}'.format(store_name))
                response = client.post('/store/{0}'.format(store_name))
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message':
                                      'A store with name "{0}" already exists.'.format(store_name)},
                                     json.loads(response.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                client.post('/store/{0}'.format(store_name))
                self.assertIsNotNone(StoreModel.find_by_name(store_name))

                response = client.delete('/store/{0}'.format(store_name))
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'}, json.loads(response.data))
                self.assertIsNone(StoreModel.find_by_name(store_name))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                client.post('/store/{0}'.format(store_name))
                response = client.get('/store/{0}'.format(store_name))
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'items': [], 'name': store_name}, json.loads(response.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                self.assertIsNone(StoreModel.find_by_name(store_name))

                response = client.get('/store/{0}'.format(store_name))
                self.assertEqual(response.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'}, json.loads(response.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                store_id = 1
                client.post('/store/{0}'.format(store_name))

                item_name = 'Tablet'
                item_price = 99.99
                ItemModel(item_name, item_price, store_id).save_to_db()

                response = client.get('/store/{0}'.format(store_name))
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'name': store_name,
                                      'items': [{'name': item_name,
                                                 'price': item_price}]},
                                     json.loads(response.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                store_id = 1
                client.post('/store/{0}'.format(store_name))

                item_name = 'Tablet'
                item_price = 99.99
                ItemModel(item_name, item_price, store_id).save_to_db()

                item_name2 = 'Chrome Book'
                item_price2 = 199.99
                ItemModel(item_name2, item_price2, store_id).save_to_db()

                response = client.get('/store/{0}'.format(store_name))
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'name': store_name,
                                      'items': [{'name': item_name, 'price': item_price},
                                                {'name': item_name2, 'price': item_price2}]},
                                     json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                pass
