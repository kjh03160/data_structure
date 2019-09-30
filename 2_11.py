from linked_slist import Slist

def repeat_num_sum(class1, class2):
    result = 0
    class1_length = class1.length()
    class2_length = class2.length()
    refer1 = class1.head
    i = 0

    while i < class1_length:
        refer2 = class2.head
        j = 0
        while j < class2_length:
            if (refer1.item == refer2.item):
                result += refer1.item
            refer2 = refer2.next
            j += 1
        refer1 = refer1.next
        i += 1
    return result

s = Slist()
s.insert_front(7)
s.insert_front(3)
s.insert_front(2)
s.insert_front(1)
s.print_list()
# print(s.head.next.item)
e = Slist()
e.insert_front(9)
e.insert_front(1)
e.insert_front(7)
e.insert_front(0)
e.print_list()
print(repeat_num_sum(s, e))