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
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size
    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                    t = "{0:5s}|".format("")
            else:
                    t = "{0:-5d}|".format(k)
            s = s + t
        return s

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while self.keys[start] != None and self.keys[start] != key:
            start = (start + 1) % self.size
            if start == i:
                    return 'Full'
        return start

    def set(self, key, value=None):
        slot = self.find_slot(key)
        if slot == "Full":
            return None
        self.keys[slot] = key
        self.values[slot] = value
        return key

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        slot = self.find_slot(key)
        j = slot
        if slot == "Full" or self.keys[slot] == None:
            return None
        return_key = self.keys[slot]
        while True:
            self.keys[slot] = None
            while True:
                j = (j + 1) % self.size
                if self.keys[j] == None:
                    return key
                k = self.hash_function(self.keys[j])
                if not (slot < k <= j or j < slot < k or k <= j < slot):
                    break
            self.keys[slot] = self.keys[j]
            self.values[slot] = self.values[j]
            slot = j

    def search(self, key):
        index = self.find_slot(key)
        if self.keys[index] != "Full":
            return self.values[index]
        return None


    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)

H = HashOpenAddr()

while True:
    cmd = input().split()
    if cmd[0] == 'set':
        key = H.set(int(cmd[1]))
        if key == None: print("* H is full!")
        else: print("+ {0} is set into H".format(cmd[1]))
    elif cmd[0] == 'search':
        key = H.search(int(cmd[1]))
        if key == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'remove':
        key = H.remove(int(cmd[1]))
        if key == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            print("- {0} is removed".format(cmd[1]))
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")

# class HashOpenAddr:
#     def __init__(self, size=10):
#         self.size = size
#         self.keys = [None] * self.size
#         self.values = [None] * self.size
#
#     def __str__(self):
#         s = ""
#         for k in self:
#             if k == None:
#                 t = "{0:5s}|".format("")
#             else:
#                 t = "{0:-5d}|".format(k)
#             s = s + t
#         return s
#
#     def __iter__(self):
#         for i in range(self.size):
#             yield self.keys[i]
#
#     def find_slot(self, key):
#         i = self.hash_function(key)
#         start = i
#         while self.keys[start] != None and self.keys[start] != key:
#             start = (start + 1) % self.size
#             if start == i:
#                 return 'Full'
#         return start
#
#     def set(self, key, value=None):
#         slot = self.find_slot(key)
#         if slot == "Full":
#             return None
#         self.keys[slot] = key
#         self.values[slot] = value
#         return key
#
#     def hash_function(self, key):
#         return key % self.size
#
#     def remove(self, key):
#         slot = self.find_slot(key)
#         j = slot
#         if slot == "Full" or self.keys[slot] == None:
#             return None
#         while True:
#             self.keys[slot] = None
#             while True:
#                 j = (j + 1) % self.size
#                 if self.keys[j] == None:
#                     return key
#                 k = self.hash_function(self.keys[j])
#                 if not (slot < k <= j or j < slot < k or k <= j < slot):
#                     break
#             self.keys[slot] = self.keys[j]
#             self.values[slot] = self.values[j]
#             slot = j
#
#     def search(self, key):
#         if key in self.keys:
#             return key
#         return None
#
# H = HashOpenAddr(10)
# H.set(75, "cat")
# H.set(18, "Dog")
# H.set(75, "tiger")
# H[75] = "cat"   # H.__setitem__(75, "Cat")
# print(H[18])    # H.search(18)