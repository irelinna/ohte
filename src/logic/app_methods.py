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

    #constructor
    #sets repositories
    """The logic and structure of the application is here.
    """
    def __init__(
        
        self,
        item_repository=default_item_repository,
        user_repository=default_user_repository,
        list_repository=default_list_repository
    ):
        """Constructor

        Args:
            item_repository: Object that has methods set from the ItemRepository class. Defaults to default_item_repository.
            user_repository: Object that has methods set from the UserRepository class. Defaults to default_user_repository.
            list_repository: Object that has methods set from the ListRepository class. Defaults to default_list_repository.
        """
        print('testing 123')
        self._user = None
        self._item_repository = item_repository
        self._user_repository = user_repository
        self._list_repository = list_repository



    def create_item(self, list_id, content):
        """Creates a new item and saves it to item_repository.

        Args:
            content: Item name in string format.
            list_id: List id of the list that the item is in.

        Returns:
            The created Item-object.
        """


        return self._item_repository.create_item(list_id, content)
    


    def create_list(self, list_name):
        """Creates a new list and saves it to list_repository.

        Args:
            list_name: Name of the created list.

        Returns:
            The created List-object.
        """
       

        return self._list_repository.create_list(list_name, self._user)
    
    
    def delete_list(self, list_name):
        """Deletes the given list.

        Args:
            list_name: Name of the list to be deleted.
        """

        self._list_repository.delete_list(list_name)
    


    def get_list_id(self, list_name):
        """Get list_id when given the list's name.

        Args:
            list_name: Name of the list.

        Returns:
            list_id of the given list
        """

        list_id = self._list_repository.get_list_id(list_name)

        return list_id
    

    def add_item_to_list(self, item_name, list_name):
        """Add item to existing list.

        Args:
            item_name: Name of the item added.
            list_name: Name of the list the item should be added to.

        Returns:
            The created Item-object.
        """

        list_id = self._list_repository.get_list_id(list_name)

        return self.create_item(item_name, list_id)
    

    def find_list_by_name(self, list_name):
        """Finds list by name.

        Args:
            list_name: Name of the list.

        Returns:
            The items from the given list.
        """

        items = self._item_repository.find_items_by_list_name(list_name)
        return items


    def login(self, username, password):
        """Login method.

        Args:
            username: String representing the username of the user.
            password: String representing the password of the user.

        Raises:
            InvalidCredentialsError: Exception is raised if the username or password given are invalid.

        Returns:
            The user that has logged in.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            return False

        self._user = user

        return user

    def get_user(self):
        """Get current user.
        """
        return self._user


    def logout(self):
        """Logout method.
        """
        self._user = None


    def create_user(self, username, password, login=True):
        """Create new user.

        Args:
            username: String representing the username of the user.
            password: String representing the password of the user.
            login: True if the user is logged in. Defaults to True.

        Raises:
            UsernameExistsError: Error is raised if the username of the new user already exists in the database.

        Returns:
            The User-object just created.
        """
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