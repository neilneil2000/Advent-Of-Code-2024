class Node:
    def __init__(self, value):
        self.previous = None
        self.value = value
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError
        pointer = self.head
        while index:
            pointer = pointer.next
            index -= 1
        return pointer.value

    def append(self, value):
        """Append item to end of Linked List"""
        if self.length == 0:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            temp = self.tail
            self.tail = self.tail.next
            self.tail.previous = temp
        self.length += 1

    def prepend(self, value):
        """Place item at head of Linked List"""
        if self.length == 0:
            self.append(value)
            return

        self.head.previous = Node(value)
        self.head.previous.next = self.head
        self.head = self.head.previous
        self.length += 1

    def insert(self, value, index):
        """Insert Value at position"""
        if index > self.length or index < 0:
            raise IndexError
        if index == 0:
            after = self.head
            self.head = Node(value)
            self.head.next = after
        elif index == self.length:
            self.append(value)
            return
        else:
            pointer = self.head
            while index:
                pointer = pointer.next
                index -= 1
            pointer.previous.next = Node(value)
            pointer.previous.next.next = pointer
            pointer.previous = pointer.previous.next
        self.length += 1

    def insert_after(self, value, node):
        """Insert value after node"""
        pointer = self.head
        while pointer is not node:
            pointer = pointer.next
        pointer.next.previous = Node(value)
        pointer.next.previous.next = pointer.next
        pointer.next = pointer.next.previous
        pointer.next.previous = pointer
        self.length += 1

    def remove(self, node):
        """Remove first instance of node in Linked List"""
        pointer = self.head
        while pointer is not node:
            pointer = pointer.next
        if pointer.previous is None:
            self.head = pointer.next
        else:
            pointer.previous.next = pointer.next
        if pointer.next is None:
            self.tail = pointer.previous
        else:
            pointer.next.previous = pointer.previous
        del pointer
        self.length -= 1

    def move(self, node, after_node):
        """Move node to be positioned after_node"""
        if after_node.next is node:
            node.value.start_location = (
                after_node.value.start_location + after_node.value.length
            )
            return
        after_node.next.previous = node
        if node is not self.tail:
            node.next.previous = node.previous
            node.previous.next = node.next
        else:
            node.previous.next = None
            self.tail = node.previous
        node.next = after_node.next
        node.previous = after_node
        after_node.next = node
        node.value.start_location = (
            after_node.value.start_location + after_node.value.length
        )
        if not self.parse_check():
            raise IndexError

    def parse_check(self):
        pointer = self.head
        for _ in range(self.length):
            pointer = pointer.next
        return pointer is None
