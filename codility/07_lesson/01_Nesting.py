# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    stack = []
    for item in S:
        if item == '(':
            stack.append(0)
        elif item == ')':
            try:
                stack.pop()
            except IndexError:
                return 0
    if stack:
        return 0
    return 1