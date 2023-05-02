import unittest
from repositories.user_repository import user_repository
from entities.user import User



class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.irene = User('irene', 'irenelol')
        self.kissa = User('kissa', 'hehekissa')

    def test_create_user(self):
        user_repository.create_user(self.irene)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.irene.username)

    def test_find_all(self):
        user_repository.create_user(self.irene)
        user_repository.create_user(self.kissa)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.irene.username)
        self.assertEqual(users[1].username, self.kissa.username)

    def test_find_by_username(self):
        user_repository.create_user(self.irene)

        user = user_repository.find_by_username(self.irene.username)

        self.assertEqual(user.username, self.irene.username)
