import unittest
from repositories.list_repository import list_repository
from entities.list import List



class TestListRepository(unittest.TestCase):
    def setUp(self):
        list_repository.delete_all()
        self.lista1 = List(1,"lista1",'irene')
        self.lista2 = List(2,"lista2",'irene')

    def test_create_list(self):
        list_repository.create_list(self.lista1.list_name, self.lista1.username)
        lists = list_repository.find_all()

        self.assertEqual(len(lists), 1)
        self.assertEqual(lists[0].list_id, self.lista1.list_id)


    def test_get_list_id(self):
        list_repository.create_list(self.lista1.list_name, self.lista1.username)
        list_id = list_repository.get_list_id(self.lista1.list_name)
        self.assertEqual(list_id, self.lista1.list_id)


    def test_find_lists_by_username(self):
        list_repository.create_list(self.lista1.list_name, self.lista1.username)
        list_repository.create_list(self.lista2.list_name, self.lista2.username)

        lists = list_repository.find_lists_by_username(self.lista1.username)
        print(lists)
        self.assertEqual("irene",self.lista1.username)
