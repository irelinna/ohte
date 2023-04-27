from entities.list import List
from user_repository import user_repository
from database_connection import get_database_connection


def get_list(row):
    #find list 
    return List(row["list_id"], row["list_name"]) if row else None


class ListRepository:

    def __init__(self, connection):
        self._connection = connection


    def find_lists_by_username(self, username):
        #returns list by username
        cursor = self._connection.cursor()

        user_id = user_repository.get_user_id(username)

        cursor.execute(
            "select * from lists where user_id = ?",
            (user_id,)
        )

        row = cursor.fetchone()
        return get_list(row)

    def create_list(self, list):
        #creates a new list and returns it
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into lists (list_name, user_id) values (?, ?)",
            (list.list_name, list.user_id)
        )

        self._connection.commit()
        return list
    
    def get_list_id(self,list_name):
        #finds list id when given list name
        cursor = self._connection.cursor()

        cursor.execute(
            "select list_id from lists where list_name = ?",
            (list_name,)
        )



list_repository = ListRepository(get_database_connection())