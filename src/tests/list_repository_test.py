import unittest
from repositories.list_repository import list_repository
from entities.list import List



class TestListRepository(unittest.TestCase):
    def setUp(self):
        list_repository.delete_all()
        self.lista1 = List(1,"lista1",'irene')
        self.lista2 = List(2,"lista2",'irene')

    def test_get_list_by_name(self):
        list_repository.create_list(self.lista1.list_name, self.lista1.username)
        list_by_name = list_repository.get_list_by_name(self.lista1.list_name)
        self.assertEqual(list_by_name[1],self.lista1.list_name)

    def test_create_list(self):
        list_repository.create_list(self.lista1.list_name, self.lista1.username)
        lists = list_repository.find_all()

        self.assertEqual(len(lists), 1)
        self.assertEqual(lists[0].list_id, self.lista1.list_id)


    def test_get_list_id(self):
        list_repository.create_list(self.lista1.list_name, self.lista1.username)
        list_id = list_repository.get_list_id(self.lista1.list_name)
        self.assertEqual(list_id, self.lista1.list_id)

