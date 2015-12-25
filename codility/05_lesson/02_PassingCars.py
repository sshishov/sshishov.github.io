# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    sum = 0
    curr = 0
    for item in A[::-1]:
        if item == 1:
            curr += 1
        if item == 0:
            sum += curr
        if sum > 1000000000:
            sum = -1
            break
    return sum