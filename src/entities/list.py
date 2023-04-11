class List:
    #a class for a list, which is a collection of items

    def __init__(self, items, user=None, list_id=None):
        self.items = items
        self.user = user
        self.id = list_id