import unittest
from repositories.item_repository import item_repository
from repositories.list_repository import list_repository
from entities.item import Item



class TestItemRepository(unittest.TestCase):
    def setUp(self):
        item_repository.delete_all()
        self.banana = Item(1,1,'banana')
        self.bread = Item(2,1,'bread')

    def test_create_item(self):
        item_repository.create_item(self.banana)
        items = item_repository.find_all()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].item_id, self.banana.item_id)


    def test_get_item_id(self):
        item_repository.create_item(self.banana)
        items = item_repository.find_all()

        item_id = item_repository.get_item_id(self.banana.content)

        self.assertEqual(items[0].item_id, item_id)


    def test_find_all(self):
        item_repository.create_item(self.banana)
        item_repository.create_item(self.bread)
        items = item_repository.find_all()

        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].item_id, self.banana.item_id)
        self.assertEqual(items[1].item_id, self.bread.item_id)


    def test_find_items_by_list_name(self):
        list_repository.create_list()
        item_repository.create_item(self.banana)
        items = item_repository.find_items_by_list_name("lista1")

        self.assertEqual(items[0].item_id, self.banana.item_id)


    def test_find_items_by_list_id(self):
        item_repository.create_item(self.banana)
        item_repository.create_item(self.bread)

        items = item_repository.find_items_by_list_id(1)
        self.assertEqual(items[0][1], self.banana.item_id)
        self.assertEqual(items[1][1], self.bread.item_id)