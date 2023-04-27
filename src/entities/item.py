class Item:
    #a class for an individual item 

    def __init__(self, item_id, list_id, content):
        self.content = content
        self.list_id = list_id
        self.id = item_id