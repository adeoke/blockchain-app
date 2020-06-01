from block import Block


class Blockchain:
    """
    Blockchain: is a public ledger of transactions.
    Implemented as a list of blocks.
    Each block is a dataset of transactions
    """

    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self):
        return "Blockchain - {}".format(self.chain)

