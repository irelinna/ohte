import unittest
from repositories.item_repository import item_repository
from repositories.list_repository import list_repository
from entities.item import Item
from entities.list import List



class TestItemRepository(unittest.TestCase):
    def setUp(self):
        item_repository.delete_all()
        self.banana = Item(1,1,'banana')
        self.bread = Item(2,1,'bread')
        self.lista1 = List(1,"lista1",'irene')

    def test_create_item(self):
        item_repository.create_item(self.banana.list_id, self.banana.content)
        items = item_repository.find_all()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].item_id, self.banana.item_id)


    def test_get_item_id(self):
        item_repository.create_item(self.banana.list_id, self.banana.content)

        item_id = item_repository.get_item_id(self.banana.content)

        self.assertEqual(item_id, self.banana.item_id)


    def test_find_all(self):
        item_repository.create_item(self.banana.list_id, self.banana.content)
        item_repository.create_item(self.bread.list_id, self.bread.content)
        items = item_repository.find_all()

        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].item_id, self.banana.item_id)
        self.assertEqual(items[1].item_id, self.bread.item_id)


    def test_find_items_by_list_name(self):
        item_repository.create_item(self.banana.list_id, self.banana.content)
        list_repository.create_list(self.lista1.list_name,self.lista1.username)

        items = item_repository.find_items_by_list_name("lista1")

        self.assertEqual(items[0], self.banana.content)

    def test_get_item_by_name(self):
        item_repository.create_item(self.banana.list_id, self.banana.content)

        item = item_repository.get_item_by_name(self.banana.content)

        self.assertEqual(item,self.banana)


    def test_find_items_by_list_id(self):
        item_repository.create_item(self.banana.list_id, self.banana.content)
        item_repository.create_item(self.bread.list_id, self.bread.content)

        banana_id = item_repository.get_item_id(self.banana.content)
        bread_id = item_repository.get_item_id(self.bread.content)

        items = item_repository.find_items_by_list_id(1)
        self.assertEqual(items[banana_id].content, self.banana.content)
        self.assertEqual(items[bread_id].content, self.bread.content)