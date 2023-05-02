class Item:
     
    """A class for an individual item.

    Attributes: item_id: the id of an item
    list_id = the id of the list the item is in
    content = item name
    """

    def __init__(self, item_id, list_id, content):
        self.content = content
        self.list_id = list_id
        self.id = item_id