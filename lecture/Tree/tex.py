class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None


    def find_loc(self, key):
        if self.root == None:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            if key > v.key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def insert(self, key):
        loc = self.find_loc(key)
        if loc == None or loc.key != key:
            v = Node(key)
            if loc == None:
                self.root = v
            else:
                if loc.key < key:
                    loc.right = v
                    v.parent = loc
                else:
                    loc.left = v
                    v.parent = loc
            self.size += 1
            return v
        else:
            print("No")

    def deleteByCopying(self, v):
        left = v.left
        right = v.right
        parent = v.parent

        if left == None:
            if right:
                v.key = right.key
                v.right = right.right
            else:
                if parent:
                    if v == parent.right:
                        parent.right = None
                    else:
                        parent.left = None
                else:
                    self.root = None

        else:
            m = left
            while m.right != None:
                m = m.right
            v.key = m.key

            if m == m.parent.right:
                m.parent.right = m.left
            else:
                m.parent.left = m.left
            if m.left:
                m.left.parent = m.parent

        self.size -= 1



    def deleteByMerging(self, v):
        right = v.right
        left = v.left
        parent = v.parent

        if left == None:
            change = right

        else:
            change = m = left
            while m.right != None:
                m = m.right
            m.right = right
            if right:
                right.parent = m

        if self.root == v:
            if change:
                change.parent = None

            self.root = change

        else:
            if parent.left == v:
                parent.left = change
            else:
                parent.right = change

            if change:
                change.parent = parent
        self.size -= 1


            