class BinaryHeap:
    def __init__(self, a):  # a 는 리스트 n은 항목 수
        self.a = a
        self.N = len(a) - 1


    def create_heap(self):  # 초기 힙 만들기
        for i in range(self.N // 2, 0, -1):
            self.downheap(i)

    def insert(self, val):
        self.N += 1
        self.a.append(val)
        self.upheap(self.N)

    def delete_min(self):   # 최솟값 삭제
        if self.N == 0:
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.downheap(1)
        self.N -= 1
        return minimum

    def downheap(self, index):
        while index * 2 <= self.N:
            k = 2 * index   # 왼쪽 자식 노드
            if k < self.N and self.a[k][0] > self.a[k + 1][0]:  # 왼쪽 자식노드가 있고 왼쪽 자식노드가 크면
                k += 1  # 오른쪽 자식 노드로
            if self.a[index][0] < self.a[k][0]: # downheap으로 내려오는 것과 k와 비교해서 작으면 바꾸기 준비
                break
            self.a[index], self.a[k] = self.a[k], self.a[index]
            index = k

    def upheap(self, index):
        while index > 1 and self.a[index // 2][0] > self.a[index][0]:
            self.a[index], self.a[index // 2] = self.a[index // 2], self.a[index]
            index = index // 2

