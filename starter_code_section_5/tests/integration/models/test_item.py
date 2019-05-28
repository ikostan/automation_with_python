import os
from starter_code_section_5.models.item import ItemModel
from starter_code_section_5.tests.base_test import BaseTest


class ItemModelIntegrationTest(BaseTest):

    #  printing out the running unit test file location/name
    print("Running unit tests from: " +
          os.path.dirname(__file__) +
          '\\' + os.path.basename(__file__) +
          "\n")

    def test_crud(self):
        with self.app_context():
            name = 'product'
            price = 99.99
            item = ItemModel(name, price)
            self.assertIsNone(ItemModel.find_by_name(name))  # make sure that item does not exist in db
            item.save_to_db()  # save an item into db
            self.assertIsNotNone(ItemModel.find_by_name(name))  # make sure that item does exist in db
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name(name))  # make sure that item does not exist in db


