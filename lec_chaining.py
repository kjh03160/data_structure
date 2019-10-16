from linked_slist import Slist

class HashChain:
    def __init__(self, size):
        self.size = size
        self.H = []     # self.H = [Slist() for _ in range(size)] > list comprehension
        for i in range(size):           # 사이즈 만큼 한방향 연결리스트 삽입
            self.H.append(Slist())

