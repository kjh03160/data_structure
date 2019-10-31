from tkinter import Tk, Label, Button, Entry, StringVar
from functools import partial

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
        if i =="(" or i == ")":
            continue
        if not i.isdigit():
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


def do_something():
    value = compute_postfix(infix_to_postfix(expr.get()))
    total.set("{0:.4f}".format(value))
    return

root = Tk()
root.title("My Calculator")
expr = StringVar()
title_label = Label(root, text="My Calcualtor").grid(row=0, columnspan=2)
input_exam = Label(root, text="Space between terms: ( 3 + 2 ) * 8").grid(row=1, columnspan=2)
exp_entry = Entry(root, textvariable=expr).grid(row=2, column=0)
total_label = Label(root, text="TOTAL").grid(row=3, column=0)
total = StringVar()
total.set('0')
value_label = Label(root, textvariable=total, width=20).grid(row=3, column=1)
equal_btn = Button(root, text=' = ', width=20, command=do_something).grid(row=2, column=1)
root.mainloop()
root.destroy()