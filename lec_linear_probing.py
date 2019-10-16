"""
# Pseudo 코드
def set(key, value):    # hash 테일블에 없는 key 삽입
    i = find_slot(key)  # 만약 hash 테이블에 key 값이 존재하면 변경
    if i == Full:
        return None
    if H[i] != None:    # 이미 key 값이 존재 할 때
        H[i].value = value
    else:
        H[i].key = key
        H[i]. value = value
    return key

def find_slot(key):     # key 값을 갖고 있는 슬롯을 찾아달라
    i = f(key)          # 없으면 빈칸의 인덱스를 리턴 (f는 hash함수)
    start = i           # 한 바퀴 돌고 돌아오는 걸 확인하기 위해

    while H[i] != None and H[i].key != key: # 해당 인덱스가 비지 않았다면 and 들어있는 key 값이 찾는 값이 아니면
        i = (i + 1) % len(H)    # 인덱스가 크기를 초과 했을 경우 처음으로
        if i == start:
            return Full
    # H[i] == None or H[i].key == key
    return i

def remove(key):
    i = findslot(key)
    if i == Full or H[i] == None:
        return None
    j = i
    while True:
        H[i] = None     # 해당 인덱스 빈칸
        while True:
            j = (j + 1) % len(H)
            if H[j] == None:
                return key
            k = f(H[j])
            if not (i < k <= j or j < i <k or k <= j < i):  # 이 모든 조건을 만족하지 못하면
                break   # 이사 올 인덱스 번호 찾음
        H[i] = H[j] # 이사올 인덱스 복사
        i = j   # 이사온 아이의 빈 집으로 다시 인덱스 옮겨서 그 빈칸 메꾸기 시작

"""
class HashOpenAddr:
    def __init__(self, size = 10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def set(self, key, value):
        pass

    def find_slot(self, key):
        pass

    def remove(self, key):
        pass

    def search(self, key):      # 해당 key의 value 값
        pass

    def hash_function(self):
        pass

    def __setitem__(self, key, value):  # 딕셔너리처럼 key value를 설정하게 해주는 함수
        self.set(key, value)
    
    def __getitem__(self, key):    # 딕셔너리처럼 key 호출하면 value 리턴
        return self.search(key)

H = HashOpenAddr(10)
H.set(75, "cat")
H.set(18, "Dog")
H.set(75, "tiger")
H[75] = "cat"   # H.__setitem__(75, "Cat")
print(H[18])    # H.search(18)