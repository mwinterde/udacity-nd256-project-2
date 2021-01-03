class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LRU_Cache(object):

    """
    The cache is a dictionary that saves nodes of a doubly linked list.
    The nodes store the (key, value) tuple for each key. Their order in the
    doubly linked list represent the access order of past cache operations.
    Therefore we are able to remove the least recently used key from the
    cache if the specified capacity of the cache is reached.
    """

    def __init__(self, capacity):

        self.cache = dict()
        self.num_entries = 0
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key):
        """
        Retrieves item from provided key and returns -1 if
        it is nonexistent.
        """

        try:
            # This block will execute if key exists in cache
            node = self.cache[key]
            if node.prev:
                if node.next:
                    # Node is in the middle of the queue
                    node.prev.next = node.next
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
            else:
                if node.next:
                    # Node is head but not tail of the queue
                    node.next.prev = None
                    self.head = node.next
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
            return node.data[1]
        except KeyError:
            # This block will execute if key does not exist in cache
            return -1

    def set(self, key, value):
        """ Stores a new key, value pair in the cache """

        # Remove old entry from the cache if key already exists
        if key in self.cache:
            self.remove(key)

        # Remove last recently used key from the cache if capacity is full
        if self.num_entries == self.capacity:
            lru_key = self.get_lru_key()
            self.remove(lru_key)

        # Insert new key, value pair into the cache
        self.cache[key] = Node((key, value))
        if not self.head:
            self.head = self.cache[key]
            self.tail = self.head
        else:
            self.tail.next = self.cache[key]
            self.cache[key].prev = self.tail
            self.tail = self.cache[key]
        self.num_entries += 1

    def get_lru_key(self):
        """ Returns last recently used key of the cache """
        return self.head.data[0]

    def remove(self, key):
        """ Removes an existing key from the cache """

        # Check if key exists
        assert key in self.cache

        # Detach node from the queue
        node = self.cache[key]
        if node.prev:
            if node.next:
                # Node is in the middle of queue
                node.prev.next = node.next
            else:
                # Node is the tail but not head of queue
                node.prev.next = None
                self.tail = node.prev
        else:
            if node.next:
                # Node is the head but not tail of queue
                node.next.prev = None
                self.head = node.next
            else:
                # Node is the only element of queue
                self.head = None
                self.tail = None

        # Remove node from dictionary
        self.cache.pop(key)

        # Decrease counter
        self.num_entries -= 1


def test():
    # Test 1
    c1 = LRU_Cache(5)
    c1.set(1, 1)
    c1.set(2, 2)
    c1.set(3, 3)
    c1.set(4, 4)
    c1.set(5, 5)
    c1.get(1)
    c1.get(2)
    c1.get(3)
    c1.set(6, 6)

    assert c1.get(1) == 1
    assert c1.get(2) == 2
    assert c1.get(3) == 3
    assert c1.get(4) == -1
    assert c1.get(5) == 5
    assert c1.get(6) == 6

    # Test 2
    c2 = LRU_Cache(3)
    c2.set(1, 1)
    c2.set(2, 2)
    c2.set(3, 3)
    c2.get(1)
    c2.get(1)
    c2.get(1)
    c2.set(4, 4)

    assert c2.get(1) == 1
    assert c2.get(2) == -1
    assert c2.get(3) == 3
    assert c2.get(4) == 4

    # Test 3
    c3 = LRU_Cache(10)
    c3.set(1, 1)
    c3.set(2, 2)
    c3.set(3, 3)

    assert c3.get(1) == 1
    assert c3.get(2) == 2
    assert c3.get(3) == 3
    assert c3.get(4) == -1

    print("All tests successful")


if __name__ == '__main__':
    test()