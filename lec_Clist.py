'''

head의 tail은 맨 뒤 노드 가리키고
last의 next는 맨 앞 노드를 가리키는 원형/양방향 리스트

시작을 나타내는 special한 노드 (dummy Node) > key값은 None
key값을 봤을 때 None이면 아 이게 더미 노드구나 파악 가능

'''

class Node:
    def __init__(self, key = None): # 새로운 노드 하나는 자기 자신을 계속 가리키고 있음
        self.key = key
        self.prev = self
        self.next = self

class Clist:
    def __init__(self):
        self.head = Node()          # 더미 노드 (비어있는 리스트는 더미 노드만 있는 것!)
        self.size = 0

    def splice(self, a, b, x):  # O(1)
        '''
        a에서 b 노드까지 잘라내서 x노드 뒤에 집어 넣는 함수
        여기 x는 같은 리스트 내에 있을 수도 있고 다른 리스트일수도 있다.
        단 x는 a 와 b 사이에 있으면 안된다.
        더미 노드도 a와 b 사이에 있으면 안됨.
        이렇게 들어온다고 믿고 코드 짠다.
        '''
        ap = a.prev
        bn = b.next
        ap.next = bn
        bn.prev = ap            # 슬라이싱후 분리 완료
        xn = x.next
        a.prev = x
        b.next = xn             # 삽입 완료

    def moveAfter(self, a, x):  # 노드 a를 x 뒤로 이동 O(1)
        self.splice(a, a, x)

    def moveBefore(self, a, x): # 노드 a를 x 앞으로 이동 O(1)
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):  # 새로운 노드 만들어서 x 뒤에 삽입 O(1)
        new = Node(key)
        self.splice(new, new, x)

    def insertBefore(self, x, key): # 새로운 노드 만들어서 x 전에 삽입 O(1)
        new = Node(key)
        self.splice(new, new, x.prev)

    def pushFront(self, key):   # O(1)
        self.insertAfter(self.head, key)

    def pushBack(self, key):    # O(1)
        self.insertBefore(self.head, key)

    def remove(self, x):        # O(1)
        if x == None or self.head == x: # 아무 값이 없는게 들어오거나 더미 노드(헤드)를 지워달라고 하면
            return
        x.prev.next = x.next
        x.next.prev = x.prev

    def popFront(self):     # O(1)
        self.remove(self.head.next)

    def popBack(self):      # O(1)
        self.remove(self.head.prev)

    def join(self):
        pass

    def split(self, x):
        pass

    def search(self, x):    # 더미노드로 다시 오면 한바퀴 돌았다는 것 O(1)
        pass