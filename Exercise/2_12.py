from linked_slist import Slist

def find_middle(class1):
    class1_leng = class1.length()
    middle_point = class1_leng // 2
    i = 0
    refer = class1.head
    while i < middle_point:
        refer = refer.next
        i += 1
    return refer.item

s = Slist()
s.insert_front(7)
s.insert_front(3)
s.insert_front(2)
s.insert_front(1)
s.insert_front(0)
s.insert_front(8)
s.print_list()
print(find_middle(s))