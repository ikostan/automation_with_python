from starter_code_section_7.tests.base_test import BaseTest
from starter_code_section_7.models.store import StoreModel
from starter_code_section_7.models.user import UserModel
from starter_code_section_7.models.item import ItemModel
import json


class ItemSystemTest(BaseTest):
    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                store_name = "Electronics"
                store_id = 1
                StoreModel(store_name).save_to_db()

                item_name = "Chrome Book"
                item_price = 199.99



