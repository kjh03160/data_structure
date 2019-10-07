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


def get_token_list(expr):
    result_list = []
    conjunction = ""
    for i in expr:
        if len(i.strip()) == 0:
            continue
        if i in "+*^-/()":
            if not (len(conjunction) == 0):
                result_list.append(str(float(conjunction)))
            conjunction = ""
            try:
                if (len(result_list) == 0 and i == "-"):
                    conjunction += i
                elif (result_list[-1] in "(+/*" and i == "-"):
                    conjunction += i
                else:
                    result_list.append(i)

            except:
                result_list.append(i)
            continue
        else:
            conjunction += i
    try:
        result_list.append(str(float(conjunction)))
    except:
        pass

    return result_list


def infix_to_postfix(token_list):
    opstack = Stack()
    outstack = []
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

    return outstack


def compute_postfix(postfix):
    stack = Stack()
    split_= postfix
    for i in split_:
        if i == "(" or i == ")":
            continue
        if i in "+-*^/":
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
                result = first ** second
                stack.push(float(result))
        else:
            stack.push(float(i))

    return stack.pop()


# 아래 세 줄은 수정하지 말 것!
# expr = input()
# value = compute_postfix(infix_to_postfix(get_token_list(expr)))
# print(value)
print(infix_to_postfix("(3+2)/(2-1)*2"))
