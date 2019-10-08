class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.next = None

    def __str__(self):
        return str((self.key, self.val))    # print(b.__str__())


class Slist:
    def __init__(self):
        self.head = None
        self.size = 0
        # self.tail = None

    def push_front(self, key, val = None):                      # 스택에서 push 기능
        new_node = Node(key, val)
        new_node.next = self.head   # 앞에 있던 노드를 가리키도록
        self.head = new_node
        self.size += 1

    def push_back(self, key, val = None):                       # 만약 Node에서 tail에 관한 정보를 init 해놨다면 O(1)시간!
        new_node = Node(key, val)
        tail = self.head
        if not(tail):
            self.head = new_node
        else:
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):                                 # 스택에서 pop역할
        if self.head == None:
            return None
        val = self.head
        key = val.key
        self.head = val.next
        del val
        self.size -= 1
        return key

    def popBack(self):                          # queue 에서 deque 기능하지만 시간이 오래걸린다.
        if self.head == None:   # 노드 없을 때
            return None
        prev = None
        tail = self.head
        while tail.next != None:
            prev = tail
            tail = tail.next
        if prev == None:        # 노드가 1개
            self.head = None
            return tail
        prev.next = tail.next   # 노드 2개 이상
        key = tail.key
        self.size -= 1
        del tail
        return key

    def search(self, key):
        refer = self.head
        while refer != None:
            if key == refer.key:    # 없을 경우를 생각해야됨
                return refer
            refer = refer.next
        return refer                # None이나 refer이나 똑같음

    def remove(self, key):          # L.remove(L.search(-6))
        refer = self.head
        if refer == None:           # 빈 노드일 경우
            return None
        if refer.next == None:      # 1개의 노드 밖에 없을 때
            return self.popFront()
        prev = None
        while key != refer.key:
            prev = refer
            refer = refer.next
        prev.next = refer.next
        val = refer
        del refer
        self.size -= 1
        return val

    def __len__(self):
        return self.size

a = Slist()
a.push_back(1)
a.push_back(3)
print(a.remove(3))
print(len(a))
# print(a.popBack())
print(a.head)