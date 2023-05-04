import unittest
from repositories.list_repository import list_repository
from entities.list import List



class TestListRepository(unittest.TestCase):
    def setUp(self):
        list_repository.delete_all()
        self.lista1 = List(0,"lista1",'irene')
        self.lista2 = List(1,"lista2",'irene')

    def test_create_list(self):
        list_repository.create_list(self.lista1)
        lists = list_repository.find_all()

        self.assertEqual(len(lists), 1)
        self.assertEqual(lists[0].list_id, self.lista1.list_id)


    def test_get_list_id(self):
        list_repository.create_list(self.lista1)
        lists = list_repository.find_all()

        list_id = list_repository.get_list_id(self.lista1.list_id)

        self.assertEqual(lists[0].list_id, self.lista1.list_id)


    def test_find_lists_by_username(self):
        list_repository.create_list(self.lista1)
        list_repository.create_list(self.lista2)

        lists = list_repository.find_lists_by_username("irene")

        self.assertEqual(lists[0],self.lista1.username)


    def test_find_items_by_list_id(self):
        list_repository.create_list(self.lista1)
        list_repository.create_list(self.lista2)

        lists = list_repository.find_items_by_list_id(1)
        self.assertEqual(lists[0][1], self.lista1.list_id)
        self.assertEqual(lists[1][1], self.lista2.list_id)