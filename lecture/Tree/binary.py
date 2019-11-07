class Node:
    def __init__(self, key = None, right = None, left = None, parent = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    # left, right 둘 다 None이면 leaf Node

# 순회
def preorder(v): # v는 노드
    if v != None:
        print(v.key)        # M
        preorder(v.left)    # L
        preorder(v.right)   # R

def inorder(v):
    if v != None:
        inorder(v.left)
        print(v.key)
        inorder(v.right)

def postorder(v):
    if v != None:
        postorder(v.left)
        postorder(v.right)
        print(v.key)