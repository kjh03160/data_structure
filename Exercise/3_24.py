from Stack_linked2 import Stack as S_l
from lec_StackClass import Stack


def reverse_Stack(stack):
    for i in range(stack.size):
        for j in range(i):
            now  = stack.head
            next = now.next
            s = Stack()
            count = 0
            stack.print_stack()
            last = None
            while next != last:
                if count != 0:
                    for i in range(count):
                        s.push(stack.pop())
                temp = stack.pop()
                last = temp             # 여기서 오류. last값이 while문 다시 올때 바뀌어서 무한루프
                # print(temp)
                s.push(stack.pop())
                stack.push(temp)
                stack.push(s.pop())
                print(now.item)
                now = next
                next = now.next
                for i in range(count):
                    stack.push(s.pop())
                count += 1


    return stack.print_stack()

s = S_l()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
# print(s.size)
reverse_Stack(s)