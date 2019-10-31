# make heap
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
    for k in range(len(A) - 1, -1, -1):
        A[0], A[k] = A[k], A[0]
        heapify_down(0, n) # A[0]번 힙 성질 맞추기, n은 A 리스트의 길이
'''
