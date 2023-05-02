class List:
    
    """A class for a list, which is a collection of items.
    Attributes: list_id: the id of the list
    list_name: the name of the list
    user_id = the id of the user who made the list
    """

    def __init__(self, list_id, list_name, user_id):
        self.id = list_id
        self.name = list_name
        self.user_id = user_id