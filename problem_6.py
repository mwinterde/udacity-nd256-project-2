class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    """
    Creates new linked list that contains the union of all elements
    of llist_1 and llist_2
    """

    # Create empty result list
    union_llist = LinkedList()

    # Create empty set to keep track of elements that have already been
    # added to the result list
    used = set()

    # Append unique values of llist_1
    current = llist_1.head
    while current:
        if current.value not in used:
            union_llist.append(current.value)
            used.add(current.value)
        current = current.next

    # Append unique values of llist_2
    current = llist_2.head
    while current:
        if current.value not in used:
            union_llist.append(current.value)
            used.add(current.value)
        current = current.next

    return union_llist


def intersection(llist_1, llist_2):
    """
    Creates new linked list that contains the intersection of all elements
    of llist_1 and llist_2
    """

    # Create empty result list
    intersect_llist = LinkedList()

    # Create set with the unique values of llist_1
    llist_1_set = set()
    current = llist_1.head
    while current:
        if current.value not in llist_1_set:
            llist_1_set.add(current.value)
        current = current.next

    # Create empty set to keep track of elements that have already been
    # added to the result set
    used = set()

    # Create result set
    current = llist_2.head
    while current:
        if (current.value in llist_1_set) and (current.value not in used):
            intersect_llist.append(current.value)
            used.add(current.value)
        current = current.next

    return intersect_llist


def test():
    # Test 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    # should print 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
    print(intersection(linked_list_1, linked_list_2))
    # should print 6 -> 4 -> 21 ->


    # Test 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    # should print 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    print(intersection(linked_list_3, linked_list_4))
    # should print empty line

    # Test 3
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    print(union(linked_list_5, linked_list_6))
    # should print empty line
    print(intersection(linked_list_5, linked_list_6))
    # should print empty line

if __name__ == '__main__':
    test()