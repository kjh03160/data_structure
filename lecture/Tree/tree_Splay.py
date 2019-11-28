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