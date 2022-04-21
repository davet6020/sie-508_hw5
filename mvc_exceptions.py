class ItemAlreadyStored(Exception):
    pass

class ItemNotStored(Exception):
    pass

class NoItems(Exception):

    def __init__(self, msg):
        self.msg = msg
