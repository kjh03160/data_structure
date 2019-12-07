
class HashOpenAddr:
    collision = 0
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
    def print_perf(self):
        print("number of collsions = ", self.collision)
    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while (self.keys[i] != None) and (self.keys[i] != key):
            self.collision += 1
            i = (i + 1) % self.size
            if i == start: return None # if full
        return i
    def set(self, key, value=None):
        i = self.find_slot(key)
        if i == None: return None   # if full
        if self.keys[i] != None:    # if occupied
            self.values[i] = value
            return key
        # H[i]가 비어있는 경우, 즉 key의 item이 없다면 새로 저장함 (삽입)
        self.keys[i] = key
        self.values[i] = value
        return key
    def hash_function(self, key):
        return key % self.size
    def remove(self, key):
        i = self.find_slot(key)
        if self.keys[i] == None:
            return None
        j = i
        while True:
            self.keys[i] = self.values[i] = None    # delete from table
            while True:
                j = (j+1) % self.size
                if self.keys[j] == None:  # 자리 이동 완료!
                    return key
                k = self.hash_function(self.keys[j])
                # |    i..k..j |
                # |....j..i..k..| or |..k..j..i..|
                if not(i < k <= j or (j < i < k or k <= j < i)):
                   break
            self.keys[i], self.values[i] = self.keys[j], self.values[j]
            i = j
    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None:    # key is in table, then return key here
            return self.keys[i]
        else:                       # key is not in table
            return None             # not found
    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)
K = int(input())
A = [int(x) for x in input().split()]
H = HashOpenAddr(2*len(A)) # 해시 테이블 크기를 |A|의 2배로 설정
for a in A:
    H.set(a)
count = 0
for a in A:
    if H.search(K-a): count += 1
print(count//2)  # why count//2?
