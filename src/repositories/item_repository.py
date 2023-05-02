from entities.item import Item
from repositories.list_repository import ListRepository
from database_connection import get_database_connection


def get_item(row):

    return Item(row[item_id], row["list_id"],row["content"]) if row else None


class ItemRepository:
    """The class responsible for the item database and its commands
    """
    def __init__(self, connection):
        """The constructor of the class
        Args: 
            connection: the database connection object
        """


        self._connection = connection


    def find_items_by_list_name(self, list_name):
        
        """Returns items by list name.

        Args:
            list_name: The name of the list.

        Returns:
            Returns a list of Item-objects.
        """
        cursor = self._connection.cursor()

        list_id = ListRepository.get_list_id(list_name)

        cursor.execute(
            "select * from items where list_id = ?",
            (list_id,)
        )

        row = cursor.fetchall()
        return get_item(row)
    
    def find_items_by_list_id(self, list_id):
        """Returns items by list id.

        Args:
            list_id: The id of the list.

        Returns:
            Returns a list of Item-objects.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from items where list_id = ?",
            (list_id,)
        )

        row = cursor.fetchall()
        return get_item(row)

    def create_item(self, item):
        """Creates a new item and returns the Item-object of the new item.

        Args:
            item: the Item-object that is created in app_methods is sent here and added to database.

        Returns:
            The new item as Item-object.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into items (list_id, content) values (?, ?)",
            (item.list_id, item.content)
        )

        self._connection.commit()
        return item
    
    def get_item_id(self,content):
        """Finds item id when given item content.

        Args:
            content: item name

        Returns: 
            Returns item_id of given item
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select item_id from items where content = ?",
            (content,)
        )
        item_id = cursor.fetchone()
        return item_id
    
    def find_all(self):
        """Returns all existing items.
        Returns:
            A list of Item-objects.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from items")

        rows = cursor.fetchall()

        return list(map(get_item, rows))
    
    def delete_all(self):
        """Deletes all items.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from items")

        self._connection.commit()



item_repository = ItemRepository(get_database_connection())