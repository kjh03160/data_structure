class Node:
    def __init__(self, key, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

class Heap:
    def __init__(self, L = []):
        self.L = L

    # def __str__(self):
    #     return self.L

    def __len__(self):
        return len(self.L)

    def insert(self, key):
        pass

    def make_heap(self):
        pass

    def heapify_down(self, k, n):   # A[k]를 밑으로
        pass

    def heapify_up(self, k):
        pass

    def heap_sort(self):
        pass

    def delete_max(self):
        pass

h = Heap([2, 8, 6, 1, 10, 15, 3, 12, 11])
h.make_heap()
# print(h.L)
h.heap_sort()