from .linked_Clist import CList

def Josephus(class1, M):
    class1_first = class1.last                  # class1.last.next로 하면 삭제될 값 앞과 뒤의 값을 연결하기 힘들다
    while class1_first.next != class1_first:    # 원소가 하나가 남을 때까지 루프
        i = 1
        while i < M:
            class1_first = class1_first.next    # M이 될 때까지 pass
            i += 1
        class1_first.next = class1_first.next.next  # 삭제된 값 앞과 뒤를 연결

    return class1_first.item

s = CList()
s.insert(7)
s.insert(3)
s.insert(2)
s.insert(1)
s.insert(0)
s.insert(8)
s.print_list()
print(Josephus(s,4))
# s.print_list()