import sys

class QueueNode:
    """
    Nodes for a linked list that we use to represent the
    priority queue
    """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class TreeNode:
    """
    Nodes for the Huffman tree that we use for encoding
    and decoding of data
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class PriorityQueue:
    """
    We will use the priority queue to grow the Huffman
    tree. In this queue we store the nodes for the binary tree
    in ascending order.
    """

    def __init__(self):
        self.head = None

    def insert(self, treenode):
        """
        Inserts a treenode at the right place in the priority queue,
        meaning that the elements remain in ascending order.
        """

        if not self.head:
            # Set node as head if queue is empty
            self.head = QueueNode(treenode)
            return

        current = self.head
        if current.data.data[1] >= treenode.data[1]:
            # Set node as head if there is no larger value in the queue
            newnode = QueueNode(treenode)
            newnode.next = self.head
            self.head = newnode
            return

        while current:
            # We loop through the queue until there is a larger or equal
            # value, or we reach the tail of the queue
            if (current.next is None or current.next.data.data[1] >=
                    treenode.data[1]):
                newnode = QueueNode(treenode)
                newnode.prev = current
                newnode.next = current.next
                current.next = newnode
                return
            else:
                current = current.next
        return

    def pop(self):
        """
        Deletes and returns the treenode with the lowest value from the
        queue.
        """

        if not self.head:
            # Return None if queue is empty
            return

        # Store treenode with lowest value for the return statement
        old_head = self.head

        # Remove the treenode from the queue
        self.head = self.head.next
        if self.head:
            self.head.prev = None

        return old_head.data

    def isempty(self):
        """ Checks if queue is empty """

        return self.head == None


def append_letter_codes(node, code):
    """ Recursive function to derive letter codes from the
    Huffman Tree """

    # Create dictionary for storing the letter codes
    codes = {}

    # Base case - reaching a leaf node of the tree
    if node.data[0]:
        codes[node.data[0]] = code
        return codes

    # Traverse the tree for growing the letter codes
    codes.update(append_letter_codes(node.left, code + '0'))
    codes.update(append_letter_codes(node.right, code + '1'))

    return codes


def huffman_encoding(data):
    """
    Grows the Huffman Tree and creates an encoded
    string from the derived letter codes.
    """

    # Count frequencies per letter
    counts = dict()
    for element in data:
        if element not in counts:
            counts[element] = 1
        else:
            counts[element] += 1

    # Add treenodes to the priority queue
    # Save the letter and its frequence as tuple in the
    # data attribute of the node.
    queue = PriorityQueue()
    for tup in counts.items():
        treenode = TreeNode(tup)
        queue.insert(treenode)

    # Grow the Huffman tree
    while True:
        # Remove nodes with the lowest frequency from the priority queue
        # and create a parent node for them.
        left = queue.pop()
        right = queue.pop()
        parent = TreeNode((None, left.data[1] + right.data[1]))
        parent.left = left
        parent.right = right

        if queue.isempty():
            # Break loop if queue is empty
            break

            # Insert parent node to the priority queue
        queue.insert(parent)

    # The parent from the last loop run represents the head of the tree
    tree = parent

    # Create letter codes and the encoded string using recursion
    codes = append_letter_codes(parent, '')
    encoded_string = ""
    for char in data:
        encoded_string += codes[char]

    return encoded_string, tree


def huffman_decoding(data, tree):
    """
    Decodes the encoded data using the provided
    Huffman Tree.
    """

    # Initialize objects
    current = tree
    char = ""

    for num in data:

        # Traverse the tree
        if num == '0':
            current = current.left
        else:
            current = current.right

        # If we reach a leaf node, append letter to the decoded
        # char and again start traversal from the head of the tree
        if current.data[0]:
            char += current.data[0]
            current = tree

    return char


def test():

    # Test 1
    string = "The bird is the word"
    encoded_string, tree = huffman_encoding(string)
    decoded_string = huffman_decoding(encoded_string, tree)
    assert sys.getsizeof(int(encoded_string, base=2)) < sys.getsizeof(string)
    assert string == decoded_string

    # Test 2
    string = "aaaaaabbbbbcccccddddddd"
    encoded_string, tree = huffman_encoding(string)
    decoded_string = huffman_decoding(encoded_string, tree)
    assert sys.getsizeof(int(encoded_string, base=2)) < sys.getsizeof(string)
    assert string == decoded_string

    # Test 3
    string = "abcdefghijklmnopqrstuvwxyz"*1000
    encoded_string, tree = huffman_encoding(string)
    decoded_string = huffman_decoding(encoded_string, tree)
    assert sys.getsizeof(int(encoded_string, base=2)) < sys.getsizeof(string)
    assert string == decoded_string

    print("All tests successful")


if __name__ == '__main__':
    test()