class CList:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next

    def __init__(self):
        self.last = None
        self.size = 0

    def no_item(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        created_Node = self.Node(item, None)

        if self.is_empty():
            created_Node.next = created_Node
            self.last = created_Node
        else:
            created_Node.next = self.last.next
            self.last.next = created_Node
        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError('overFlow')
        return self.last.next.item

    def delete(self):
        if self.is_empty():
            raise EmptyError('underFlow')
        if self.size == 0:
            self.last = None

        d_ele = self.last.next
        self.last.next = d_ele.next
        self.size -= 1
        return d_ele

    def print_list(self):
        if self.size == 0:
            print("비어있음")
        else:
            x = self.last.next
            while x.next != self.last.next:
                print(x.item, "=>", end="")
                x = x.next

            print(x.item)

class EmptyError(Exception):
    pass


# s = CList()
# s.insert('pear')
# s.insert('cherry')
# s.insert('orange')
# s.insert('apple')
# s.print_list()
# print("s의 길이 : ", s.no_item())
# print('s의 첫 항목 :', s.first())
# s.delete()
# print('첫 노드 삭제 후 :', end="")
# s.print_list()