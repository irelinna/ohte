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




class AppMethods:
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
        self._list_repository = list_repository



    def create_item(self, content, list_id):
        #create a new item and save to repository

        item = Item(content=content, list_id = list_id)

        return self._item_repository.create_item(item)
    


    def create_list(self, list_name):
       
        list = List(list_name = list_name, user_id = self._user_repository.get_user_id(self._user))

        return self._list_repository.create_list(list)
    
    
    def delete_list(self, list_name):

        self._list_repository.delete_list(list_name)
    


    def get_list_id(self, list_name):

        list_id = self._list_repository.get_list_id(list_name)

        return list_id
    

    def add_item_to_list(self, item_name, list_name):

        list_id = self._list_repository.get_list_id(list_name)

        return self.create_item(item_name, list_id)
    
    def find_list_by_name(self, list_name):
        items = self._item_repository.find_items_by_list_name(list_name)
        return items


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

        user = self._user_repository.create_user(User(username, password))

        if login:
            self._user = user

        return user
    


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


app_methods = AppMethods()