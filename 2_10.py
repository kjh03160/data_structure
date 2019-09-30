from linked_slist import Slist


def sorting_by_k(class1, k):
    class1_leng = class1.length()
    i = 0

    more_than = Slist()
    less_than = Slist()

    refer = class1.head

    while i < class1_leng:
        if (refer.item <= k):
            less_than.insert_front(refer.item)
        else:
            more_than.insert_front(refer.item)
        i += 1
        refer = refer.next

    return more_than.print_list(), less_than.print_list()

s = Slist()
s.insert_front(7)
s.insert_front(8)
s.insert_front(3)
s.insert_front(2)
s.insert_front(1)
s.print_list()
sorting_by_k(s, 3)