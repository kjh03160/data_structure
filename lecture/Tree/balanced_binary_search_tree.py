'''
AVL Tree
모든 노드 v에서 (v의 오른쪽 서브트리 높이 - v의 왼쪽 서브트리 높이) 의 절대값이 항상 <= 1 인 트리


Red-Black Tree  -> 가장 효율, 많이 쓰이지만 가장 복잡

Splay Tree  -> 평.균.적으로 O(log n), 간단

3개의 tree에 맞게 형태를 바꾸는 함수를 rotate라고 함 -> 트리가 한 쪽에 치우치지 않게 해줌

'''

def rotateRight(z):     # z에서 바꾸기 > O(1)
    if z == None:
        return None

    x = z.left
    if x == None:
        return

    b = x.right
    x.parent = z.parent

    if z.parent:    # z의 부모가 있다면
        if z.parent.key < x.key:
            z.right = x
        else:
            z.left = x

    x.right = z
    z.parent = x

    z.left = b
    if b:
        b.parent = z

    if z == self.root:
        self.root = x

    # 필요 시 각 노드(x, z, 루트까지의 노드)의 height 정보 업데이트