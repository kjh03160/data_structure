from lec_StackClass import Stack

def parenthesis(input):
    input_list = input.split()
    s = Stack()
    for i in input_list:
        if i in "})":
            if s.isEmpty():
                return False
            else:
                s.pop()
        else:
            s.push(i)
    if not s.isEmpty():
        return False
    return True

a = "{ { ( ) { ( ) } } }"
print(parenthesis(a))
b = "{ { ( ) { ( ) } ) () }"
print(parenthesis(b))