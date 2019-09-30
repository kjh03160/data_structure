class Slist:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)

        else:
            self.head = self.Node(item, self.head)

        self.size += 1

    def insert_after(self, item, refer):
        refer.next = self.Node(item, refer.next)            # Slist.Node ? self.Node?
        self.size += 1

    def del_front(self):
        if self.is_empty():
            raise EmptyError("Underflow")
        else:
            self.head = self.head.next
            self.size -= 1

    def del_after(self, refer):
        if self.is_empty():
            raise EmptyError("Underflow")
        else:
            refer.next = refer.next.next
            self.size -= 1

    def search(self, target):
        start = self.head
        for i in range(self.size):
            if start.item == target:
                return i
            else:
                start = start.next
        return None

    def print_list(self):
        start = self.head
        while start:
            if start.next != None:
                print(start.item, "=>", end="")
            else:
                print(start.item)
            start = start.next

class EmptyError(Exception):
    pass

# s = Slist()
# s.insert_front('orange')
# s.insert_front('apple')
# s.insert_after('cherry', s.head.next)
# s.insert_front('pear')
# s.print_list()
# print('cherry는 %d번째' % s.search('cherry'))
# print('kiwi는', s.search('kiwi'))
# print('배 다음 노드 삭제 후:\t\t', end="")
# s.del_after(s.head)
# s.print_list()
# print('첫 노드로 망고, 딸리 삽입 후 :\t', end='')
# s.insert_front('mango')
# s.insert_front('strawberry')
# s.print_list()
# s.del_after(s.head.next.next)
# print('오렌지 다음 노드 삭제 후:\t', end='')
# s.print_list()

def Slist_sort(class1, class2):
    class1_length = class1.length()
    class2_length = class2.length()
    new_Slist = Slist()
    i = 1
    j = 1
    refer1 = class1.head
    refer2 = class2.head
    while (i < class1_length) or (j < class2_length):
        if (refer1.item < refer2.item):
            new_Slist.insert_front(refer1.item)
            refer1 = refer1.next
            i += 1
        else:
            new_Slist.insert_front(refer2.item)
            refer2 = refer2.next
            j += 1

    if i < class1_length:
        while i < class1_length:
            new_Slist.insert_after(refer1.item, refer2)
            refer1 = refer1.next
            i += 1
    else:
        while j < class2_length:
            new_Slist.insert_after(refer2.item, refer1)
            refer2 = refer2.next
            j += 1
    return new_Slist

def make(class1, class2):
    # class1_length = class1.length()
    class2_leng = class2.length()
    # print(class2_leng)
    # i = 1
    j = 1
    refer1 = class1.head
    refer2 = class2.head
    # print(refer1.item)
    # print(refer2.item)
    while j < class2_leng:
        if (refer2.item > refer1.item):
            while refer1.next == None:
                if (refer1.next.next.item < refer2.item):
                    refer1 = refer1.next.next
                    continue
            class1.insert_after(refer2.item, refer1)
            print(refer2.item,  refer1.item)
            refer2 = refer2.next
            refer1 = refer1.next.next
            j += 1
        else:
            class1.insert_front(refer2.item)
            # print(refer2.item)
            refer2 = refer2.next
    return class1.print_list()

s = Slist()
s.insert_front(7)
s.insert_front(3)
s.insert_front(2)
s.insert_front(1)
# print(s.head.next.item)
e = Slist()
e.insert_front(9)
e.insert_front(6)
e.insert_front(4)
e.insert_front(0)

