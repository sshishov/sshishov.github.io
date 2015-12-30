# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    array = []
    for item in S:
        if array:
            if item in ('(', '[', '{'):
                array.append(item)
            else:
                if (item == ')' and array[-1] == '(') or (item == ']' and array[-1] == '[') or (item == '}' and array[-1] == '{'):
                    array.pop()
                else:
                    return 0
        else:
            if item in ('(', '[', '{'):
                array.append(item)
            else:
                return 0
    if array:
        return 0
    return 1