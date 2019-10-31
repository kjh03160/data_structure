'''
Infix to postfix
'''


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


def infix_to_postfix(infix):
    opstack = Stack()
    outstack = []
    token_list = infix.split(' ')

    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)

        elif token == ')':
            while opstack.top() != "(":
                val = opstack.pop()
                outstack.append(val)
            opstack.pop()

        elif token in '+-/*^':
            if opstack.isEmpty():
                opstack.push(token)
            else:
                while not opstack.isEmpty() and prec[opstack.top()] >= prec[token]:
                    val = opstack.pop()
                    outstack.append(val)
                opstack.push(token)
        else:  # operand일 때
            outstack.append(token)

    while not (opstack.isEmpty()):
        val = opstack.pop()
        outstack.append((val))

    return " ".join(outstack)


infix_expr = "3 + 2 ^ 4 / ( 6 - 1 ) * 1"
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)