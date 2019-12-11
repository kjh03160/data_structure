# make Tree
# heapify-down을 이용하여

'''
heapify-down(k) 는 A[k]을 밑으로 내려보냄
맨 밑의 것부터 시작
자식 노드 중 힙 성질을 만족하는 것과 바꿈
3개로 구성된 작은 서브트리로 시작해서 점점 윗 단계에서 내려가면서.


def heapify_down(k): # A[k] -> 조건 위치로
    while 2*k+1 < n: # A[k] != leaf
        L = 2 * k + 1   # 왼쪽 자식
        R = 2 * k + 2   # 오른쪽 자식

        if A[L] > A[k]:
            m = L
        else:
            m = k

        if R < n and A[R] > A[m]: 오른쪽 자식이 존재하고
            m = R

        if m != k:  # 자식이 더 클경우
            A[k], A[m] = A[m], A[k]
            k = m
        else:
            break
    # 돌고 나면 서브트리 1개 밑으로 정렬 됨

def make_heap(A):
    n = len(A)
    for k in range((n // 2) - 1, -1, -1): # (n // 2) - 1 는 마지막 반은 leaf이기 때문에 저렇게 넣어도 됨.
        heapify_down(k)

# 힙 정렬
MAX값이 계속 필요할 때 유용
[15, 12, 6, 11, 10, 2, 3, 1, 8]
A[0] 과 A[-1]을 바꿈 > 그럼 맨 마지막 15는 정렬 된 상태  n을 하나 줄이고 다음 과정
8이 맨 앞으로 왔으니 A[0] 에 관해서 heapify_down > log n
이 과정을 반복하면 오름차순 정렬 완료 > n 번 반복
O(n log n)

def heap_sort:
    n = len(A)
    for k in range(len(A) - 1, -1, -1):
        A[0], A[k] = A[k], A[0]
        n -= 1
        heapify_down(0, n) # A[0]번 힙 성질 맞추기, n은 A 리스트의 길이

def heapify_up(k):  # O(log n)
# A[k]를 위로 올라가면서 위치 찾기
# 자기 부모를 찾아가면서 본인보다 작으면 자리 바꾼다.
    while k > 0 and A[k] >= A[(k-1)//2]:
    A[k], A[(k-1)//2] = A[(k-1)//2], A[k]
    k = (k - 1) // 2



def insert(key):
 # append(key)가 우선 실행됨 -> 힙 조건 성립 안될 수 있음
 # 이건 올라가면서 맞춰줘야 된다.
    A.append(key)   # A는 힙 리스트
    heapify_up(len(A) - 1)      # 인덱스를 값으로 넘겨준다


def deleteMax(A):    # Max 값 찾아서 리턴해주고 지워달라 O(log n)
    if len(A) == 0: return None
    key = A[0]
    A[0], A[-1] = A[-1], A[0]
    A.pop()
    heapify_down(0, len(A))
    return key

Min_Heap > 부등호만 바꾸자

파이썬에선 이미 구현되어 있음
import heapq  >>> Min Heap
h = []
heappush(h, key) => insert
만약 key 값을 음수로 넣어버리면 Max Tree 처럼 할 수 있다.

heappop(h)  => deleteMin
heapify(A)  => make_heap
h[0] => 최솟값



Max, Min 값을 찾는데 가장 효율적
만약 어떤 값을 찾는데 사용하는 것은 좋지 않음

'''


class Heap:
    def __init__(self, L=[]):
        self.A = L

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):   # A[k]를 밑으로 내려보내기 n은 Heap의 크기
        while 2 * k + 1 < n:
            left_node = 2 * k + 1
            right_node = 2 * k + 2
            if self.A[k] < self.A[left_node]:
                m = left_node
            else:
                m = k

            if right_node < n and self.A[m] < self.A[right_node]:
                m = right_node

            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break

    def make_heap(self):
        n = len(self.A)
        for k in range((n // 2) - 1, -1, -1):  # (n // 2) - 1 는 마지막 반은 leaf이기 때문에 저렇게 넣어도 됨.
            self.heapify_down(k, n)

    def heap_sort(self):
        n = len(self.A)
        for k in range(n - 1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n -= 1
            # print(self.A)
            self.heapify_down(0, n)  # A[0]번 힙 성질 맞추기, n은 A 리스트의 길이

S = [3,4,5,32,62,32,3,345,454,3]
H = Heap(S)
H.make_heap()
print(H)

H.heap_sort()
print(H)















