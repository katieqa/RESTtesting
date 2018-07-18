from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):

    def test_create_item(self):
        i = ItemModel('Name', 10.00)

        self.assertEqual('Name', i.name, "error msg if they aren't the same")
        self.assertEqual(10.00, i.price)


    def test_json(self):
        i = ItemModel('Name', 10.00)
        expected = {'name': 'Name', 'price': 10.00}

        self.assertDictEqual(expected, i.json(), "JSON received does not match expected. Received {} expected {}".format(i.json(), expected))

    def test_find_by_name(self):
        pass

    def test_save_to_db(self):
        pass

    def test_delete_from_db(self):
        pass

