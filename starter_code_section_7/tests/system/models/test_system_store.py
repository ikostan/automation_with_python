from starter_code_section_7.tests.base_test import BaseTest
from starter_code_section_7.models.store import StoreModel
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

    def create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                client.post('/store/{0}'.format(store_name))
                response = client.post('/store/{0}'.format(store_name))
                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({"message": "An error occurred creating the store."}, json.loads(response.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                store_name = 'test_store'
                StoreModel(store_name).save_to_db()

                self.assertIsNotNone(StoreModel.find_by_name(store_name))

                response = client.delete('/store/{}'.format(store_name))
                self.assertIsNone(StoreModel.find_by_name(store_name))
                self.assertEqual(response.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'}, json.loads(response.data))


    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                pass

    def store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                pass

