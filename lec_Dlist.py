class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.key)

class DList:
    def __init__(self):
        self.head = Node()  # 더미 노드
        self.size = 0



