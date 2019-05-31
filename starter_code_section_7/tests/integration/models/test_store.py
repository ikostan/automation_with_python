from starter_code_section_7.models.store import StoreModel
from starter_code_section_7.models.item import ItemModel
from starter_code_section_7.tests.integration.integration_base_test import BaseTest


class StoreIntegrationTestCase(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')
        self.assertListEqual([], store.items.all(), "The store's items list is not empty")

    def test_crud(self):
        with self.app_context():
            name = 'test'
            store = StoreModel(name)
            self.assertIsNone(StoreModel.find_by_name(name))
            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name(name))
            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name(name))

    def test_store_relationships(self):
        with self.app_context():
            name = 'test'
            store = StoreModel(name)
            item_name = 'test_item'
            item = ItemModel(item_name, 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, item_name)

    def test_store_json(self):
        name = 'test'
        store = StoreModel(name)
        expected = {
            'name': name,
            'items': []
        }

        self.assertDictEqual(expected, store.json())

    def test_store_json_items(self):
        with self.app_context():
            name = 'test'
            store = StoreModel(name)

            item_name = 'test_item'
            item = ItemModel(item_name, 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': name,
                'items': [{'name': item_name, 'price': 19.99}]
            }

            self.assertDictEqual(expected, store.json())

