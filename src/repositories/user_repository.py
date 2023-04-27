from entities.user import User
from database_connection import get_database_connection

# these are pretty much straight from the material 
# because there's not really a better way of doing these

def get_user(row):
    #find user 
    return User(row["username"], row["password"]) if row else None


class UserRepository:

    def __init__(self, connection):
        self._connection = connection


    def find_by_username(self, username):
        #returns user by username
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()
        return get_user(row)

    def create_user(self, user):
        #creates a new user and returns it
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()
        return user
    
    def get_user_id(self,username):
        #finds user id when given username
        cursor = self._connection.cursor()

        cursor.execute(
            "select user_id from users where username = ?",
            (username,)
        )



user_repository = UserRepository(get_database_connection())