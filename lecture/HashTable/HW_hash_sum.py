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
        index = self.hash_function(key)
        start = index
        while self.keys[index] != None and self.keys[index] != key:
            index = (index + 1) % self.size
            if start == index:
                return None
        return index


    def set(self, key, value=None):
        index = self.find_slot(key)
        if index == None:
            return None
        if self.keys[index] == None:
            self.keys[index] = key
            self.values[index] = value

        else:
            self.values[index] = value
        return key


    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        index = self.find_slot(key)
        if index == None or self.keys[index] == None:
            return None
        start = index

        while True:
            self.keys[start] = None
            while True:
                index = (index + 1) % self.size
                if self.keys[index] == None:
                    return key
                k = self.hash_function(self.keys[index])
                if not(start < k <= index or index < start < k or k <= index < start):
                    break
            self.keys[start] = self.keys[index]
            self.values[start] = self.values[index]
            start = index

    def search(self, key):
        index = self.find_slot(key)
        if index == None:
            return None
        if self.keys[index] == key:
            return key

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)

# 해시테이블 두 수 찾기

result = int(input())
cand = input().split()
print(cand)
print(len(cand))
count = 0

H = HashOpenAddr(int(len(cand) * 1.5))
for i in cand:
    H.set(int(i))
print(H)
for i in H:
    if i == None or result // 2 == result - i:
        continue
    find_key = result - i
    value = H.search(find_key)
    if value == None:
        continue
    print("val : %d find : %d result : %d" % (i, value, result))

    count += 1
    H.remove(value)
    H.remove(i)
    print(H)

print(count)