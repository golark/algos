class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = None

    # append
    # append a new node to the tail
    def append(self, data):

        # append to Head if we dont have any Nodes
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
            return

        # traverse to tail
        n = self.head
        while n.next is not None:
            n = n.next

        # append
        new_node = Node(data)
        n.next = new_node
        new_node.next = None

    # remove_index
    # remove node at given index
    def remove_index(self, index):

        # find node with index
        count = 0
        node = self.head
        while count != index:
            if node.next is None:
                raise Exception("remove_index: index is larger than the node count")
            node = node.next
            count += 1

        # remove index
        node.next = node.next.next

    # remove
    # remove node given the key
    def remove(self, key):

        # key is head
        if self.head.data == key:
            self.head = self.head.next
            return

        # traverse through the linked list
        # find node that matches key
        node = self.head.next
        prev = self.head
        while node is not None:

            # remove if we find a match
            if node.data == key:
                prev.next = node.next
                return

            prev = node
            node = node.next

    # count
    # count number of nodes
    def count(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next

        return count

    # display
    # display nodes
    def display(self):

        node = self.head
        while node is not None:
            print(f'data: {node.data}, next: {node.next}')
            node = node.next

    # reverse
    def reverse(self):

        prev = None
        node = self.head
        while node is not None:
            # reverse reference
            next_node = node.next
            node.next = prev

            # move to next node
            prev = node
            node = next_node

        self.head = prev

    # reverse_recursive
    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if cur is None:
                return prev

            next_node = cur.next
            # reverse nodes
            cur.next = prev

            # move nodes
            prev = cur
            cur = next_node
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(self.head, None)

    # remove_duplicates
    # set based algorithm to remove multiple occurrence of data
    def remove_duplicates(self):

        cur = self.head
        prev = None
        s = set()
        while cur is not None:

            if cur.data not in s:
                # add to set
                s.add(cur.data)
            else:
                # remove node
                prev.next = cur.next

            # move nodes
            prev = cur
            cur = cur.next
