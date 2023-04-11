class Item:
    #a class for an individual item 

    def __init__(self, content, user=None, item_id=None):
        self.content = content
        self.user = user
        self.id = item_id