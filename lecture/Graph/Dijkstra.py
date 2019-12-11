"""
min Heap 자료구조를 기반

def Dijkstra(G):
    n, m = numbers of nodes and edges of G
		s = source node, simply 0
    d = [0, inf, ..., inf]
    parent = [0, NULL, ..., NULL]
    H = make_heap(nodes v of G with key d[v])
    while len(H): # n iterations
        u = H.deleteMin()
        for each v adjacent to u: # m edges are scanned in total
            if (u, v) is an edge of G:
                if d[u] + cost(u, v) < d[v]:
                    d[v] = d[u] + cost(u, v)
                    parent[v] = u
                    H.decreaseKey(v, d[v])
    return dist, parent

수행시간
-Min Heap : insert, delete > 각 노드 수 n * log n
            relax, decreaseKey > 각 엣지 E * log n = n^2 * log n
            총 O(n^2 * log n)
-Fibonacci Heap : insert, delete > Min Heap과 같음
                  decreaseKey > O(1)
            총 O(n^2)
"""

class Heap:
    def __init__(self, L = []):
        self.L = L

    def __str__(self):
        return str(self.L)

    def heapify_down(self, k, n):   # A[k]를 밑으로 내려보내기 n은 Heap의 크기
        while 2 * k + 1 < n:
            left_node = 2 * k + 1
            right_node = 2 * k + 2
            if self.L[k] < self.L[left_node]:
                m = left_node
            else:
                m = k

            if right_node < n and self.L[m] < self.L[right_node]:
                m = right_node

            if m != k:
                self.L[k], self.L[m] = self.L[m], self.L[k]
                k = m
            else:
                break

    def make_heap(self):
        n = len(self.L)
        for i in range(n // 2, -1, -1):
            self.heapify_down(i, n)


    def heap_sort(self):
        n = len(self.L)
        for k in range(n - 1, -1, -1):
            self.L[0], self.L[k] = self.L[k], self.L[0]
            n -= 1
            # print(self.L)
            self.heapify_down(0, n)


    def heapify_up(self, k):  # O(log n) A[k]를 위로 올리기
        while k > 0 and self.L[k][1] < self.L[(k - 1) // 2][1]:
            self.L[(k - 1) // 2], self.L[k] = self.L[k], self.L[(k - 1) // 2]
            k = (k - 1) // 2

    def __len__(self):
        return len(self.L)

    def deleteMin(self):
        if len(self.L) == 0:
            return None

        self.L[0], self.L[-1] = self.L[-1], self.L[0]
        val = self.L.pop()
        self.heapify_down(0, len(self.L))
        return val

    def insert(self, key):
        self.L.append(key)
        self.heapify_up(len(self.L) - 1)

    def decrease_key(self, v, dist):
        self.insert([dist, v])
        self.heapify_up(-1)



"""
def relax(u, v):
	if d[v] > d[u] + cost(u, v):
		d[v] = d[u] + cost(u, v)
		p[v] = u"""


def Dijkstra(G, v_num):
    dist = [0] + [0xFFFFFFFF for i in range(v_num - 1)]
    parent = [None for i in range(v_num)]

    H = Heap()
    H.insert([dist[0], 0])

    while len(H) != 0:
        u = H.deleteMin()
        if u[0] > dist[u[1]]:
            continue
        else:
            u = u[1]
        for i in G[u]:
            v = i[0]
            w = i[1]
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                H.decrease_key(v, dist[v])

    return dist, parent




v_num = int(input()) # 노드의 개수
e_num = int(input()) # 엣지 개수
"""
엣지 정보 u, v, w
(u, v) w 가중치
u와 v는 노드 번호
w는 가중치로 양의 정수
"""

graph = [[] for i in range(v_num)]

for i in range(e_num):
    u, v, w = map(int, input().split())
    graph[u].append((v, w,))

print(graph)
# print(graph)
# H = Heap([13,4,5,2,1])
#
# print(H.heap_sort())
# print(H)
dist, parent = Dijkstra(graph, v_num)

for i in dist:
    if i == 0xFFFFFFFF:
        i = "inf"
    print(i, end= " ")

