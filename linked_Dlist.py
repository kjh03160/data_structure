class DList:
    class Node:
        def __init__(self, item, prv, next):
            self.item = item
            self.prv = prv
            self.next = next
    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_before(self, refer, item):
        if self.is_empty():
            self.head = self.Node(item, self.head, self.tail)
        else:
            content = self.Node(item, refer.prv, refer)
            refer.prv.next = content
            refer.prv = content
        self.size += 1

    def insert_after(self, refer, item):
        content = self.Node(item, refer, refer.next)
        refer.next.prv = content
        refer.next = content
        self.size += 1

    def delete(self, x):
        x.prv.next = x.next
        x.next.prv = x.prv
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print("비어있음")
        else:
            tail = self.head.next
            while tail != self.tail:
                if (tail.next != self.tail):
                    print(tail.item, '<=>', end="")
                else:
                    print(tail.item)
                tail = tail.next


s = DList()
s.insert_after(s.head, 'apple')
s.insert_before(s.tail, 'orange')
s.insert_before(s.tail, 'cherry')
s.insert_after(s.head.next, 'pear')
s.print_list()
print("마지막 노드 삭제 후:\t", end="")
s.delete(s.tail.prv)
s.print_list()
print('맨 끝에 포도 삽입 후:\t', end="")
s.insert_before(s.tail, 'grape')
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()


