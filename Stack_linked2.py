class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    class Node:
        def __init__(self, data, link):
            self.data = data
            self.next = link

    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        new_node = self.Node(data, self.head)
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next
        return ret_data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.data