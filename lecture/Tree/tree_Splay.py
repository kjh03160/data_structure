'''
Splay Tree
    - 높이가 O(log n)이 아님!
    - search, insert, delete
    - 평균 시간 : O(log n)

Splay 연산 # 노드 x를 여러번의 rotation을 이용해 root 노드로 만드는 작업
def splay(x):
    x가 왼쪽에 붙어있는가 오른쪽에 붙어있는가에 따라 rotate 방향 정해서
    루트까지 올라감


search(key) -> splay 까지 해서 root로 만들어버림 > cache와 같이 한번 찾으면 다시 찾을 확률 높아서
def serach(key):
    x = BST.search(key)
    splay(x)

insert(key)도 똑같이
def insert(key):
    y = BST.insert(key)
    splay(key)

delete
def delete(x):
    splay(x)
    m = largest in L
    splay(m)    # L의 루트가 됨
    m.right = R
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
            if v != None:
                print(v.key, end=' ')
                self.preorder(v.left)
                self.preorder(v.right)

    def inorder(self, v):
            if v != None:
                self.inorder(v.left)
                print(v.key, end=' ')
                self.inorder(v.right)

    def postorder(self, v):
            if v != None:
                self.postorder(v.left)
                self.postorder(v.right)
                print(v.key, end=' ')

    def find_loc(self, key):
            if self.size == 0:
                return None
            p = None
            v = self.root
            while v:
                if v.key == key:
                    return v
                elif v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
            return p

    def search(self, key):
            p = self.find_loc(key)
            if p and p.key == key:
                return p
            else:
                return None

    def insert(self, key):
        v = None
        p = self.find_loc(key)
        if p == None:
            v = self.root= Node(key)
        elif p.key != key:
            v = Node(key)
            v.parent = p
            if p.key > key:
                p.left = v
            else:
                p.right = v
        if v != None:
            self.size = self.size + 1
        return v

class SplayTree(Tree):
    def rotateLeft(self, z):
        if z == None:
            return None

        x = z.right
        if x == None:
            return

        b = x.left
        x.parent = z.parent

        if z.parent:  # z의 부모가 있다면
            if z.parent.key < x.key:
                z.parent.right = x
            else:
                z.parent.left = x

        x.left = z
        z.parent = x

        z.right = b
        if b:
            b.parent = z

        if z == self.root:
            self.root = x

    def rotateRight(self, z):
        if z == None:
            return None

        x = z.left
        if x == None:
            return

        b = x.right
        x.parent = z.parent

        if z.parent:  # z의 부모가 있다면
            if z.parent.key < x.key:
                z.parent.right = x
            else:
                z.parent.left = x

        x.right = z
        z.parent = x

        z.left = b
        if b:
            b.parent = z

        if z == self.root:
            self.root = x

    def splay(self, v):
        while v != self.root:
            if v.parent == self.root:
                if self.root.right == v:
                    self.rotateLeft(v.parent)
                else:
                    self.rotateRight(v.parent)

            else:
                if v == v.parent.left and v.parent == v.parent.parent.left:
                    self.rotateRight(v.parent)
                elif v == v.parent.right and v.parent == v.parent.parent.right:
                    self.rotateLeft(v.parent)
                else:
                    if v == v.parent.left:
                            self.rotateRight(v.parent)
                            self.rotateLeft(v.parent)
                    else:
                            self.rotateLeft(v.parent)
                            self.rotateRight(v.parent)

        return v	# return the root after splaying

    def search(self, key):
        v = super(SplayTree, self).search(key)
        if v: # splay v
                self.root = self.splay(v)
        return v

    def insert(self, key):
        v = super(SplayTree, self).insert(key)
        if v:  # splay v
            self.root = self.splay(v)
        return v

    def delete(self, x):
        x = self.splay(x)
        l = x.left
        r = x.right
        if l:
            while l.right != None:
                l = l.right
            m = l
            self.splay(m)
            m.right = r
            self.root = m
            if r:
                r.parent = m
        else:
            if r:
                r.parent = None
            self.root = r

    def preorder(self, v):
        super(SplayTree, self).preorder(v)

    def postorder(self, v):
        super(SplayTree, self).postorder(v)

    def inorder(self, v):
        super(SplayTree, self).inorder(v)

T = SplayTree()

while True:
    cmd = input().split()
    if cmd[0] == 'in':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'del':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'find':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")