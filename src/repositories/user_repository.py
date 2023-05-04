from entities.user import User
from database_connection import get_database_connection



def get_user(row):
    
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """The class responsible for the user database and its commands
    """
    def __init__(self, connection):
        """The constructor of the class
        Args: 
            connection: the database connection object
        """

        self._connection = connection
        

    def find_by_username(self, username):
        """Returns user by username.

        Args:
            username: The username of the user that should be returned.

        Returns:
            Returns a User-object, if the user is in the database, otherwise returns None.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()
        return get_user(row)


    def create_user(self, user):
        """Creates a new user and returns the User-object of the new user.

        Args:
            User: the User-object that is created in app_methods is sent here and added to database.

        Returns:
            The new user as User-object.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()
        return user
    
    
    def find_all(self):
        """Returns all existing users.
        Returns:
            A list of User-objects.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user, rows))
    
    def delete_all(self):
        """Deletes all users.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()



user_repository = UserRepository(get_database_connection())