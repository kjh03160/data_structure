class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)


class BST:
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

    def search(self, key):
        parent = self.find_loc(key)
        if parent and parent.key == key:
            return parent
        return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key:  # p is parent of v
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
        # else:
        #     return None
        self.size += 1
        return v

    def deleteByMerging(self, x):
        a, b, parent = x.left, x.right, x.parent
        if a == None:
            c = b

        else:
            c = a
            m = a
            while m.right != None:
                m = m.right
            if b != None:
                b.parent = m
            m.right = b

        if x == self.root:
            self.root = c
            if c != None:
                c.parent = None

        else:
            if parent.left == x:
                parent.left = c

            else:
                parent.right = c

        if c != None:
            c.parent = parent
        self.size -= 1

    def deleteByCopying(self, x):
        a, b, parent = x.left, x.right, x.parent
        if a:
            cand_node = a
            while cand_node.right != None:
                cand_node = cand_node.right

        elif b:
            cand_node = b
            while cand_node.left != None:
                cand_node = cand_node.left
        else:
            cand_node = None

        if cand_node:
            x.key = cand_node.key
            # if a == cand_node:
            # 		x.left = cand_node.left
            # if b == cand_node:
            # 		x.right = cand_node.right

            if cand_node == cand_node.parent.left:
                if b == cand_node.parent:
                    cand_node.parent.left = cand_node.right
                else:
                    cand_node.parent.left = cand_node.left

                if cand_node.left:
                    cand_node.left.parent = cand_node.parent

            else:
                if a == cand_node.parent:
                    cand_node.parent.right = cand_node.left
                else:
                    cand_node.parent.right = cand_node.right

                if cand_node.right:
                    cand_node.right.parent = cand_node.parent

        else:
            if x == self.root:
                self.root = None
            else:
                if x == parent.right:
                    parent.right = None

                else:
                    parent.left = None
            x.parent = None
        self.size -= 1

    def height(self, x):
        if x == None:
            return -1
        else:
            left = self.height(x.left)
            right = self.height(x.right)
            return max(left, right) + 1

    def number(self, x):
        if x == None:
            return 0
        else:
            left = self.number(x.left)
            right = self.number(x.right)
            result = left + right + 1
            return result

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


T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * key {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'number':
        num = T.number(T.search(int(cmd[1])))
        if num == 0:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print(" * key {0} has {1} descendants".format(cmd[1], num))
    elif cmd[0] == 'Rleft':
        z = T.search(int(cmd[1]))
        if z == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(z)
            print(" * Rotated left at node {0}".format(cmd[1]))
            T.inorder(T.root)
            print()
    elif cmd[0] == 'Rright':
        z = T.search(int(cmd[1]))
        if z == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(z)
            print(" * Rotated right at node {0}".format(cmd[1]))
            T.inorder(T.root)
            print()
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
