class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = self
        self.prev = self

    def __str__(self):
        return str(self.key)

class DList:
    def __init__(self):
        self.head = Node()  # 더미 노드
        self.size = 0

    def splice(self, a, b, x):
        a.prev.next = b.next
        b.next.prev = a.prev

        x.next.prev = b
        b.next = x.next
        x.next = a
        a.prev = x

    def moveafter(self, a, x):
        self.splice(a, a, x)

    def movebefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertafter(self, x, key):
        new = Node(key)
        self.moveafter(new, x)

    def insertbefore(self, x, key):
        new = Node(key)
        self.movebefore(new, x)

    def pushfront(self, key):
        self.insertafter(self.head, key)
        self.size += 1

    def pushback(self, key):
        self.insertbefore(self.head, key)
        self.size += 1

    def remove(self, node):
        if node == None or node == self.head:
            return "Error"
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node





    # def pushback(self, key):
    #     new = Node(key)
    #     if self.size == 0:
    #         self.head.next = new
    #         new.prev = self.head
    #
    #     else:
    #         self.tail.next = new
    #         new.prev = self.tail
    #
    #     self.tail = new
    #     new.next = self.head
    #     self.head.prev = new
    #
    #     self.size += 1
    #
    # def remove(self, key):
    #     refer = self.head
    #     while refer.next != None:
    #         if refer.key == key:
    #             return_key = refer.key
    #             refer.prev.next = refer.next
    #             refer.next.prev = refer.prev
    #             del refer
    #             self.size -= 1
    #             return return_key
    #         else:
    #             refer = refer.next

    def print_list(self):
        if self.size == 0:
            print("비어있음")
        else:
            tail = self.head
            while tail.next != self.head:
                print(tail.key,"> ",end="")
                tail = tail.next
            print(tail.key)


# d = DList()
# d.pushback(1)
# d.pushback(2)
# d.pushback(3)
# d.remove(2)
# d.print_list()
