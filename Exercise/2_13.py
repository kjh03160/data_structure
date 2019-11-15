from linked_slist import Slist

def find_cycle(class1):
    class1_leng = class1.length()
    refer = class1.head
    for i in range(class1_leng):
        if(refer.next == refer):
            return True
        refer = refer.next
    return False

s = Slist()
s.insert_front(7)
s.insert_front(3)
s.insert_front(2)
s.insert_front(1)
s.insert_front(0)
s.insert_front(8)
print(find_cycle(s))