class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

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
                if not (start < k <= index or index < start < k or k <= index < start):
                    break
            self.keys[start] = self.keys[index]
            self.values[start] = self.values[index]
            start = index

    def search(self, key):
        index = self.find_slot(key)
        if index == None:
            return None
        if self.keys[index] == key:
            return self.values[index]

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)
"""
여러분의 중간고사 성적은 만점 57점에 평균 32점이고 표준편차는 7.9입니다
중간고사 성적은 다음과 같은 해시 테이블 H에 저장되었습니다.

슬롯의 갯수 m = 80
key = 학번의 왼쪽에서 4번째 자리수 * 학번의 마지막 네 자리수
예: 학번이 201801234라고 한다면 key 값은 8 * 1234 = 9872 임!
value = 중간고사 점수
해시 함수 f(key) = key % m
저장 방법은 open addressing의 linear probing 방법입니다

전체 수강생의 key 값은 data/student_id.txt에 저장되어 있습니다

수강생의 학번을 나름 보호하기 위해 학번을 그대로 사용하지 않고 위에서처럼 두 부분의 곱으로 표현했습니다!

파일 data/student_id.txt에 나타난 key 값을 순서대로 set 함수를 이용해 해시 테이블 H에 입력했고, 
해시 테이블의 H[0]부터 H[m-1]까지 차례로 한 줄에 하나의 값(value 값 = 중간고사 점수)을 파일 data/hashed_score.txt에 저장했습니다

파일을 읽을 때에는
open("data/student_id.txt", "r") 식으로 하면 됩니다.
이 파일을 읽어 여러분의 학번을 이용해 점수를 확인하기 바랍니다.
set 함수를 이용해 학생들의 key 값과 짝이 되는 중간고사 점수가 어느 슬롯에 저장되는지 시뮬레이션하여 알아내면 됩니다. ^^

"""

H = HashOpenAddr(80)
stid = open("student_id.txt", "r")
value = open("hashed_score.txt", "r")

st_list = []
value_list = []

for i in stid:
    st_list.append(int(i.strip()))

for i in value:
    if i.isdigit():
        value_list.append(float(i.strip()))
    else:
        value_list.append(i.strip())

stid.close()
value.close()

length = len(st_list)
index = 0
while length != index:
    H.set(st_list[index], value_list[H.find_slot(st_list[index])])
    # print(st_list[index], value_list[H.find_slot(st_list[index])])
    index += 1

a = input("학번 : ")
a = int(a[3]) * int(a[5:])
# print(a)
print(H.search(a))


