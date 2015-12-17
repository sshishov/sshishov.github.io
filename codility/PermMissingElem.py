# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    lenA = len(A)
    sumA = sum(A)
    return (lenA + 2) * (lenA + 1) // 2 - sumA
