import unittest
from repositories.item_repository import item_repository
from entities.item import Item



class TestUserRepository(unittest.TestCase):
    def setUp(self):
        item_repository.delete_all()
        self.banana = Item(1,1,'banana')
        self.bread = Item(2,1,'bread')

    def test_create_item(self):
        item_repository.create_item(self.banana)
        items = item_repository.find_all()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].item_id, self.banana.item_id)

    def test_find_all(self):
        item_repository.create_item(self.banana)
        items = item_repository.find_all()

        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].item_id, self.banana.item_id)
        self.assertEqual(items[1].item_id, self.bread.item_id)

    def test_get_item_id(self):
        item_repository.create_item(self.banana)

        item_id = item_repository.get_item_id(self.banana.content)

        self.assertEqual(item_id, self.banana.item_id)

    def test_find_items_by_list_id(self):
        item_repository.create_item(self.banana)

        items = item_repository.find_items_by_list_id(self.banana.list_id)
        self.assertEqual(items[0].item_id, self.banana.item_id)
        self.assertEqual(items[1].item_id, self.bread.item_id)