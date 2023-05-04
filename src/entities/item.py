class Item:
     
    """A class for an individual item.

    Attributes: item_id: the id of an item
    list_id = the id of the list the item is in
    content = item name
    """

    def __init__(self, item_id, list_id, content):
        self.item_id = item_id
        self.list_id = list_id
        self.content = content