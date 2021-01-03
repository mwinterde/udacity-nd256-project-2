import hashlib
from datetime import datetime

class Block:
    """
    A block consists of some data and a timestamp. If exists, it can be
    linked to some previous block.
    """

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        Creates a hash code for the block based on the timestamp and
        the data of the block.
        """

        sha = hashlib.sha256()
        hash_str = str(self.timestamp).encode('utf-8') + str(self.data).encode(
            'utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


class Blockchain:
    """
    A blockchain consists of several blocks. Each block can be
    accessed over a dictionary using its hash code. The sequence of
    blocks can be derived from the previous_hash attribute of the
    blocks itselves. Therefore, the only information we need to have
    access to full information of the blockchain is the hash code of
    the most recent block, which will be stored in the head attribute
    of the blockchain.
    """

    def __init__(self):

        self.head = None
        self.blocks = dict()
        self.num_blocks = 0

    def add_block(self, data):
        """ Adds a new block to the blockchain """

        # Get current timestamp and hash code of the previous block if it exists
        timestamp = datetime.utcnow()
        if not self.head:
            previous_hash = None
        else:
            previous_hash = self.head

        # Create new block and keep track of changes in the blockchain
        block = Block(timestamp, data, previous_hash)
        self.head = block.hash
        self.blocks[block.hash] = block
        self.num_blocks += 1

    def print_blockchain(self):
        """ Helper function to print the full blockchain"""

        # Start with the most recent block
        current_hash = self.head
        counter = self.num_blocks

        # Print blocks until we reach the end of the blockchain
        while (current_hash):
            current_block = self.blocks[current_hash]
            print("================================")
            print(f"#{counter}")
            print(f"HASH: {current_hash}")
            print(f"TS:   {current_block.timestamp}")
            print(f"DATA: {current_block.data}")
            print("")
            current_hash = current_block.previous_hash
            counter -= 1

def test():
    chain = Blockchain()
    chain.add_block({'a': 1, 'b': 2, 'c': 3})
    chain.add_block({'a': 4, 'b': 5, 'c': 6, 'd': 7})
    chain.add_block({'b': 8, 'c': 9, 'd': 10})
    chain.print_blockchain() # should print the full blockchain

if __name__ == '__main__':
    test()