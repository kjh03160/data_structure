from lec_StackClass import Stack

def postifx(input):
    s = Stack()
    output = []

    prior = {
        "+" :1,
        "-": 1,
        "*": 2,
        "/": 2,
        "(": 0,

    }

    for i in input:
        if i in "(*/+-)":
            if s.isEmpty():
                s.push(i)
            else:
                if i == ")":
                    while s.top() != "(":
                        output.append(s.pop())
                    s.pop()
                    continue
                elif i == "+-*/":
                    if s.isEmpty():
                        s.push(i)
                    else:
                        print(i)
                        print(s.items)

                        while not s.isEmpty() and prior[i] <= prior[s.top()]:
                            output.append(s.pop())
                s.push(i)

        else:
            output.append(i)
    while len(s) != 0:
        output.append(s.pop())
    return output

print(postifx("(3+2)/(2-1)*2"))