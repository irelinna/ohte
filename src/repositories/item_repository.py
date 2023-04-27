from entities.item import Item
from list_repository import list_repository
from database_connection import get_database_connection


def get_item(row):
    #find item 
    return Item(row["item_id"], row["list_id"],row["content"]) if row else None


class ItemRepository:

    def __init__(self, connection):
        self._connection = connection


    def find_items_by_list(self, list_name):
        #returns items by list name
        cursor = self._connection.cursor()

        list_id = list_repository.get_list_id(list_name)

        cursor.execute(
            "select * from items where list_id = ?",
            (list_id,)
        )

        row = cursor.fetchall()
        return get_item(row)

    def create_item(self, item):
        #creates a new item and returns it
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into items (list_id, content) values (?, ?)",
            (item.list_id, item.content)
        )

        self._connection.commit()
        return item
    
    def get_item_id(self,content):
        #finds item id when given item content
        cursor = self._connection.cursor()

        cursor.execute(
            "select item_id from items where content = ?",
            (content,)
        )



item_repository = ItemRepository(get_database_connection())