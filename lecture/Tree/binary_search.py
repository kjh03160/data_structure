'''
find_loc(k) > k가 들어갈 자리를 찾는것 => HashTable.find_slot 비슷
k가 있으면 k노드를 반환, 없으면 k가 들어갈 자리의 부모 노드 반환

h = O(log n) 을 유지하는 트리 > Balanced BST라고 부름
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0 # 내려갈 수 있는 높이
        self.size = 0   # 나를 포함한 내 자손들의 개수 = 왼쪽 자식 노드 사이즈 + 오른쪽 자식 노드 사이즈 + 1
        # height 와 size는 postorder로 순회하면 한 번에 지정 가능
        # height = max(left_height, right_heigth) + 1

class BST:
    def __init__(self):
        self.root = None
        self.size = self.root.size   # 전체 트리의 size

    def compute_height(self, v):
        if v == None:
            return -1
        else:
            left = self.compute_height(v.left)
            right = self.compute_height(v.right)
            v.height = max(left, right) + 1
            return v.heigth

    def search(self, key):  # 있으면 노드를 리턴, 없으면 NOne O(h) = O(n)
        v = self.root
        while v:    # None이 아닐 때까지 > 자식노드가 없을 때 까지
            if v.key == key:
                return v
            elif v.key > key:
                v = v.left
            else:
                v = v.right
        return None

    def find_location(self, key):   # search, hash_table의 find_slot 과 비슷 O(h)
        if self.size == 0:
            return None
        parent = None
        v = self.root
        while v:
            if v.key == key:
                return v
            elif v.key > key:
                parent = v
                v = v.left
            else:
                parent = v
                v = v.right
        return parent

    def insert(self, key):  # O(h) => O(n)
        parent = self.find_location(key)
        if parent == None or parent.key != key: # 앞 조건이 F일때만 뒷 조건 수행 -> parent.key 가 오류 일으킬 가능성 없음
            v = Node(key)
            if parent == None:
                self.root = v
            else:
                if parent.key > key:
                    parent.left = v
                else:
                    parent.right = v
                v.parent = parent
            self.size += 1
            return v
        else:   # 이미 key 값이 존재 할 때
            print("key already exists")
            return None

    def deleteByMerging(self, x):   # O(h)  log n <= h <= n-1     =>    O(n)
        a, b, pt = x.left, x.right, x.parent
        if a == None:
            c = b   # x를 대체할 노드
        else:
            c = a
            m = a
            while m.right != None:  # O(h)
                m = m.right
            if b:   # b 가 None 이 아닐 때
                b.parent = m
            m.right = b

        if self.root == x:  # x가 root일 때
            self.root = c
            if c:
                c.parent = None
        else:
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
        if c:
            c.parent = pt
        self.size -= 1
        pass

    def deleteByCopying(self, x):   # O(h) = O(n)
        '''
        x 를 없애지 말고 밑의 왼쪽 노드에서 가장 큰 값으로 대체하기
        왼쪽 노드가 없다면 오른쪽 노드가
        대체된 노드의 자리를 왼쪽 노드가 차지
        :return:
        '''
        pass

    def number(self, v):    # 자신을 포함해서 자손이 몇개 있는지
        pass

    def succ(self, x):      # x노드의 키 값 다음으로 큰 노드 찾기
        '''
        x 노드의 오른쪽으로 가서 왼쪽 밑으로 계속 내려감
        만약 오른쪽 노드가 없다면 parent로 올라가기
        자식이 부모의 왼쪽 노드일 때까지 올라가야함
        그러면 그 부모가 successor
        '''
        pass

    def pred(self, x):      # x노드 키 값 다음으로 작은 노드 찾기
        pass