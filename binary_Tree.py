class Node:
    def __init__(self, item, left = None, right = None, parent = None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, n):  # n은 노드
        if n != None:
            print(n.item)
            self.preorder(n.left)
            self.preorder(n.right)

    def inorder(self, n):
        if n != None:
            self.inorder(n.left)
            print(n.item)
            self.inorder(n.right)

    def postorder(self, n):
        if n != None:
            self.postorder(n.left)
            self.postorder(n.right)
            print(n.item)

    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(t.item)
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1