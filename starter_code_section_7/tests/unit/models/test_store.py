from starter_code_section_7.models.store import StoreModel
from starter_code_section_7.tests.unit.unit_base_test import BaseUnitTestCase


class StoreUnitTest(BaseUnitTestCase):
    def test_create_store(self):
        name = 'test store'
        store = StoreModel(name)
        self.assertEqual(name, store.name,
                         'The name of the store after creation does not equal the '
                         'constructor argument.')


