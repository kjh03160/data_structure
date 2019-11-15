from linked_slist import Slist as Slist

def Slist_sort(class1, class2):
    class1_length = class1.length()
    class2_length = class2.length()
    new_Slist = Slist()
    new_Slist_head = new_Slist.head
    i = 1
    j = 1
    refer1 = class1.head
    refer2 = class2.head
    while (i < class1_length) or (j < class2_length):
        if (refer1.item > refer2.item):
            new_Slist.insert_after(refer1.item, new_Slist_head)
            refer1 = refer1.next
            print(new_Slist_head)
            new_Slist_head = new_Slist.head.next
            i += 1
        else:
            new_Slist.insert_after(refer2.item, new_Slist_head)
            new_Slist_head = new_Slist.head.next
            refer2 = refer2.next
            j += 1

    if i < class1_length:
        while i < class1_length:
            new_Slist.insert_after(refer1.item, refer2)
            refer1 = refer1.next
            i += 1
    else:
        while j < class2_length:
            new_Slist.insert_after(refer2.item, refer1)
            refer2 = refer2.next
            j += 1
    return new_Slist.print_list()

if __name__ == '__main__':
    s = Slist()
    s.insert_front(7)
    s.insert_front(3)
    s.insert_front(2)
    s.insert_front(1)
    # print(s.head.next.item)
    e = Slist()
    e.insert_front(9)
    e.insert_front(6)
    e.insert_front(4)
    e.insert_front(0)

    Slist_sort(s, e)