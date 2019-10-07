class Stack:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def push(self,item):
        global top
        global size
        top = self.Node(item, top)
        size += 1

    def peek(self):
        if size != 0:
            return top.item

    def pop(self):
        global top
        global size
        if size != 0:
            top_item = top.item
            top = top.next
            size -= 1
            return top_item

    def print_stack(self):
        print('top ->\t', end="")
        p = top
        while p:
            if p.next != None:
                print(p.item, '->', end="")
            else:
                print(p.item, end="")
            p = p.next
        print()

# top = None
# size = 0
# push('apple')
# push('orange')
# push('cherry')
# print_stack()
# print(peek())
