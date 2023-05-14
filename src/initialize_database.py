from database_connection import get_database_connection


def drop_tables(connection):
    """Deletes tables from database.
    Args: 
        connection: the database connection object
    """
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)

    cursor.execute("""
        drop table if exists lists;
    """)

    cursor.execute("""
        drop table if exists items;
    """)

    connection.commit()


def create_tables(connection):
    """Creates database tables.
    Args: 
        connection: the database connection object
    """

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE users (username TEXT PRIMARY KEY UNIQUE, password TEXT NOT NULL);
    """)

    cursor.execute("""
        CREATE TABLE lists (list_id INTEGER PRIMARY KEY, list_name TEXT NOT NULL, username TEXT, FOREIGN KEY (username) REFERENCES users (username));
    """)

    cursor.execute("""
        CREATE TABLE items (item_id INTEGER PRIMARY KEY, list_id INTEGER, content TEXT NOT NULL, FOREIGN KEY (list_id) REFERENCES lists (list_id));
    """)

    connection.commit()


def initialize_database():
    """Initializes the database.
    """

    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
