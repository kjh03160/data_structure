class Stack:
    def __init__(self):
        self.item = []
        self.size = 0

    def push(self, value):
        self.item.append(value)
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.item.pop()
        return print("Stack is Empty")

    def peek(self):
        if self.size != 0:
            return self.item[-1]
        return print("Stack is Empty")

    def __len__(self):
        return len(self.item)

    def isEmpty(self):
        return self.__len__() == 0

