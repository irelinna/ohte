from entities.list import List
from repositories.user_repository import UserRepository
from database_connection import get_database_connection


def get_list(row):
    #find list 
    return List(row["list_id"], row["list_name"]) if row else None


class ListRepository:
    """The class responsible for the list database and its commands
    """

    def __init__(self, connection):
        """The constructor of the class
        Args: 
            connection: the database connection object
        """

        self._connection = connection


    def create_list(self, list):
        """Creates a new list and returns the List-object of the new list.

        Args:
            List: the List-object that is created in app_methods is sent here and added to database.

        Returns:
            The new list as List-object.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into lists (list_name, username) values (?, ?)",
            (list.list_name, list.username)
        )

        self._connection.commit()
        return list
    

    def get_list_id(self,list_name):
        """Finds list id when given list name.

        Args:
            list_name: The name of the list where the id should be returned from.

        Returns: 
            The list_id of the wanted list.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select list_id from lists where list_name = ?",
            (list_name,)
        )
        list_id = cursor.fetchone()
        return list_id
    
    def find_all(self):
        """Returns all lists.
        Returns:
            A list of List-objects.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from lists")

        rows = cursor.fetchall()

        return list(map(get_list, rows))


    def find_lists_by_username(self, username):
        """Returns lists by username.

        Args:
            username: The username of the user whose created lists should be returned.

        Returns:
            Returns a list of List-objects.
        """
        cursor = self._connection.cursor()

        username = UserRepository.get_user_id(username)

        cursor.execute(
            "select * from lists where username = ?",
            (username,)
        )

        row = cursor.fetchall()
        return get_list(row)


    def delete_list(self, list_name):
        """Deletes list.

        Args:
            list_name: The name of the list that should be deleted.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from lists where list_name = ?",
            (list_name,)
        )
        self._connection.commit()

    def delete_all(self):
        """Deletes all lists.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from lists")

        self._connection.commit()



list_repository = ListRepository(get_database_connection())