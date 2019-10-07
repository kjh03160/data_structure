class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    class Node:
        def __init__(self, data, link):
            self.item = data
            self.next = link

    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        new_node = self.Node(data, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        ret_data = self.head.item
        self.head = self.head.next
        self.size -= 1
        return ret_data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.item

    def print_stack(self):
        print('top ->\t', end="")
        p = self.head

        while p:
            if p.next != None:
                print(p.item, '->', end="")
            else:
                print(p.item, end="")
            p = p.next
        print()

# s = Stack()
# s.push(1)
# s.push(2)
# s.print_stack()
# s.pop()
# s.print_stack()