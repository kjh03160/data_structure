'''
5가지 조건 만족
    1. 노드는 Red / Black
    2. 루트 노드는 항상 Black
    3. 리프 노드는 None이고 항상 Black
    4. Red 노드의 자식은 둘 다 Black
    5. 루트부터 리프까지 Black height는 동일해야함.
        -> 자신을 제외하고 밑으로 내려가면서 어떤 리프까지 가는 경로 상의 Black 노드의 개수가 같아야함

    cf) 2-3-4 Tree (2, 3, 4 는 자식 수 / 모든 리프 노드는 같은 레벨에 있음)
        - 이진 트리 아님
        - 자식이 2개 > key 1개, 자식 3개 > key 2개, 자식 4개 > key 3개 (가장 작은 값 왼쪽, 중간값 중간, 큰 값 오른쪽)

        2-3-4 Tree 를 Red/Black Tree로 바꾸기
            1. key 값이 2개면 작은 것이 부모, 큰 것이 부모의 오른쪽 자식 / 3개면 중간값 부모, 작은 값 왼쪽 자식, 큰 값 오른쪽 자식
            2. 리프 노드는 위의 노드와 비교하여 어디에 붙을 지 결정 후 1번 과정 거침
            3. 루트는 블랙, 분리 된 노드에서 부모는 Black, 자식은 Red

        하나의 노드는 2개의 레벨로 분리 될 수 있음 > 2-3-4 트리가 h이면 R/B트리는 높이가 2h를 벗어나지 않음
        2-3-4 Tree의 h는 최대 log2 (n + 1) -> 만약 자식의 수가 2일 경우가 최대임
        RedBlack Tree Height <= 2h ---> 2 log n = O(log n)

'''

"""
def insert(self, v):
    BST.insert(v)
    x.color = red
    
    if T.root == x:
        x.color = black
    
    elif x.parent.color == black:
        pass
    
    elif x.parent.color == red: # 루트까지 올라가면서 체크해야됨
        if x.uncle.color == red:    # 부모의 형제 노드가 빨간색 일때
            x.parent.parent.color = red
            x.uncle.color, x.parent.color = black, black
        
        else:                       # 부모의 형제 노드가 검은색 일때 > grandparent 노드는 그러면 검은색 일 수 밖에 없음
                                    # x를 끌어올리고 parent를 밑으로 내림
            BST.rotateLeft(x.parent)
            BST.rotateright(x.parent)   # 원래의 grandparent(현 x.parent)를 기준
            x.color = black
            x.right.color = red         # x.right는 원래의 grandparent
            # 2번의 rotation
        

def delete(self, x):    # rotation 최대 3번만 하면 됨
    pass                # AVL에서는 최대 log n번
    
"""