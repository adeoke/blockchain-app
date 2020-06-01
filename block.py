class Block:
    """
    Block: is a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Block - {}".format(self.data)

