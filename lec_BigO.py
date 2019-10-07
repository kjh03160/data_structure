from random import randint, seed
import time


def prefixSum1(X, n):
    # code for prefixSum1
    new_array = []
    for i in range(n):
        value = randint(-999, 999)
        X.append(value)
        result = 0
        for j in range(len(X)):
            result += X[j]
            new_array.append(result)


def prefixSum2(X, n):
    # code for prefixSum2
    new_array = []
    for i in range(n):
        value = randint(-999, 999)
        X.append(value)
        result = sum(X)
        new_array.append(result)

seed()

n = randint(1000, 100000)
print("n = %d" % n)
before = time.process_time()
prefixSum1([], n)
after = time.process_time()
print(after - before)

before = time.process_time()
prefixSum2([], n)
after = time.process_time()
print(after - before)

