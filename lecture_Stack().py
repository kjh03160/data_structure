class Stack:
    def __init__(self):
        self.item = []
        self.size = 0

    def push(self, val):
        self.item.append(val)
        self.size += 1

    def pop(self):
        try:
            return self.item.pop()
        except IndexError:
            print("Stack is empty")

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def __len__(self):
        return self.size
    def top(self):
        try:
            return self.item[-1]
        except IndexError:
            print("Stack is empty")

# pseudo code
def parChecker(parSeq):
    s = Stack()
    for i in parSeq:
        if i == "(":
            s.push(i)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    return False

a = input()
print(parChecker(a))