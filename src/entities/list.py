class List:

    """A class for a list, which is a collection of items.
    Attributes: list_id: the id of the list
    list_name: the name of the list
    user_id = the id of the user who made the list
    """

    def __init__(self, list_id, list_name, username):
        self.list_id = list_id
        self.list_name = list_name
        self.username = username
