import unittest
import os
from starter_code.models.item import ItemModel


class ItemModelTestCase(unittest.TestCase):

    print("Running unit tests from: " +
          os.path.dirname(__file__) +
          '\\' + os.path.basename(__file__) +
          "\n")

    def setUp(self):
        self.name = 'product'
        self.price = 99.99
        self.itemModel = ItemModel(self.name, self.price)

    def test_init(self):
        self.assertEqual(self.name,
                         self.itemModel.name,
                         "ItemModel 'name' arg value {0} does not match the inserted data {1}".
                         format(self.itemModel.name, self.name))
        self.assertEqual(self.price,
                         self.itemModel.price,
                         "ItemModel 'price' arg value {0} does not match the inserted data {1}".
                         format(self.itemModel.price, self.price))

    def test_json(self):
        pass


if __name__ == '__main__':
    unittest.main()
