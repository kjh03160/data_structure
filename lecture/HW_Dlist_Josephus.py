from lec_Dlist import DList

def Josephus(n, k):
    D = DList()
    for i in range(1, n + 1):
        D.pushback(i)

    refer = D.head.next # 1부터 시작함
    while True:
        if D.size == 1:
            break
        target = 1
        while target < k:
            # print(refer)
            refer = refer.next
            if refer.key == None:
                refer = refer.next
            target += 1
        refer_key = refer
        refer = refer.next
        if refer.key == None:
            refer = refer.next
        D.remove(refer_key)
    return refer.key

# n, k = map(int, input().split())
# print(n, k)
print(Josephus(6, 3))