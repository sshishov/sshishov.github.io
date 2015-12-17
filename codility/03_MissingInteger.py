# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

from collections import defaultdict

def solution(A):
    # write your code in Python 2.7
    lenA = len(A)
    dictCount = defaultdict(int)
    for item in A:
        dictCount[item] += 1
    start = 1
    while True:
        if dictCount[start] == 0:
            return start
        start += 1
