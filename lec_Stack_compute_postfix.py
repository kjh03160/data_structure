class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def compute_postfix(postfix):
    stack = Stack()
    input_list = postfix.split()
    for i in input_list:
        if not i.isdigit():
            print(i)
            print(stack.items)
            second = stack.pop()
            first = stack.pop()
            op = i
            if op == "+":
                result = first + second
                stack.push(result)
            elif op == "-":
                result = first - second
                stack.push(result)
            elif op == "*":
                result = first * second
                stack.push(result)
            elif op == "/":
                result = first / second
                stack.push(result)
        else:
            stack.push(int(i))

    return stack.top()

a = input()
print("%.4f" % compute_postfix(a))



