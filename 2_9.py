from linked_slist import Slist

def Slist_sort(class1):
    class1_length = class1.length()
    new_Slist = Slist()
    i = 0
    refer1 = class1.head
    while (i < class1_length):
            new_Slist.insert_front(refer1.item)
            refer1 = refer1.next
            i += 1

    return new_Slist.print_list()

def reverse(link):
    now = link.head
    prev = None
    next = now.next

    for i in range(link.size):
        if next != None:
            next_tem = next
            now.next = prev

            next_tem.next = next.next

            prev = now
            now = next_tem
            next = next_tem.next

    now.next = prev
    link.head = now

    return link

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

    Slist_sort(s)