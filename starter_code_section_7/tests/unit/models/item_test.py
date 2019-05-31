from starter_code_section_7.tests.unit.unit_base_test import BaseUnitTestCase
from starter_code_section_7.models.item import ItemModel


class ItemTest(BaseUnitTestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.store_id, 1,
                         "The store_id of the item after creation does not equal the constructor argument.")
        self.assertIsNot(item.store)

    def test_item_json(self):
        item = ItemModel('test', 19.99, 1)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(
            item.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}."
                .format(item.json(), expected))

