from binary_search import BST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

class AVL(BST):
    def insert(self, key):
        v = super(AVL, self).insert(key)
        while v:
            pass

    def delete(self, u):
        v = super(AVL, self).deleteByMerging(u)
        while v != None:
            self.compute_height(v)
            if abs(v.left.height - v.right.height) > 1:
                z = v
                if z.left.height >= z.right.height:
                    y = z.left
                else:
                    y = z.right

                if y.left.height >= y.right.height:
                    x = y.left
                else:
                    x = y.right
                v = self.rebalance(x, y, z)
            v = v.parent