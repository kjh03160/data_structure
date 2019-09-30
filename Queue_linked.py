class Queue:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, val):
        if self.is_empty():
            new_node = self.Node(val, self.rear)
            self.head = new_node
        else:
            new_node = self.Node(val, None)
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if (self.head != None):
            return_val = self.head
            self.head = self.head.next
            self.size -= 1
            return return_val.item
        else:
            print("Queue is Empty")

    def peek(self):
        return self.head.item

    def display(self):
        current = self.Node(None, self.head)
        while current.next:
            current = current.next
            print(current.item, "> ", end="")
        print()

class EmptyError(Exception):
    pass

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
