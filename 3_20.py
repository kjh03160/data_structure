from lec_StackClass import Stack

def postfix_cal(input):
    s = Stack()
    for i in input:
        if i in "+-*/":
            second = int(s.pop())
            first = int(s.pop())
            if i == "+":
                s.push(first + second)
            elif i == "-":
                s.push(first - second)
            elif i == "*":
                s.push(first * second)
            else:
                s.push(first / second)
        else:
            s.push(i)
    return s.pop()

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

    return outstack

a = "( 3 - 2 ) * 3 - ( 3 / ( 1 + 2 ) )"
a = infix_to_postfix(a)
print(a)
print(postfix_cal(a))