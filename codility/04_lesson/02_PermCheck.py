# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from collections import defaultdict

def solution(A):
    # write your code in Python 2.7
    lenA = len(A)
    sumA = sum(A)
    dictCount = defaultdict(int)
    for item in A:
        dictCount[item] += 1
    if max(dictCount.values()) == 1 and lenA * (lenA + 1) // 2 == sumA:
        return 1
    return 0
