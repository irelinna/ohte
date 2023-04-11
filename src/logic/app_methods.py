from entities.item import Item
from entities.user import User
from entities.list import List

from repositories.item_repository import (
    item_repository as default_item_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)

from repositories.list_repository import (
    list_repository as default_list_repository
)




class appMethods:
    #the logic and structure of the application is here

    #constructor
    #sets repositories
    def __init__(
        self,
        item_repository=default_item_repository,
        user_repository=default_user_repository,
        list_repository=default_list_repository
    ):
        
        self._user = None
        self._item_repository = item_repository
        self._user_repository = user_repository

    def create_item(self, content):
       
        item = Item(content=content, user=self._user)

        return self._item_repository.create(item)
    
    def create_list(self, content):
       
        list = List(content=content, user=self._user)

        return self._list_repository.create(list)


    def login(self, username, password):

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def get_user(self):
        return self._user


    def logout(self):
        self._user = None


    #create new user and check for existing username

    def create_user(self, username, password, login=True):
        username_exists = self._user_repository.find_by_username(username)

        if username_exists:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user
    


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


app_methods = appMethods()