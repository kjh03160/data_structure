from collections import deque

def palinadrome(input):
    d = deque()
    for i in input:
        d.append(i)
    while d.__len__() > 1:
        if not d.pop() == d.popleft():
            return False
    return True

def is_palindrome(word):
    for string in range(0, len(word) // 2):
        if word[string] == word[len(word) - string - 1]:
            if string == (len(word) // 2) - 1:
                return True
        else:
            return False


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
a = "stars"
print(palinadrome(a))