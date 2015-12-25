# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    A = sorted(A)
    lenA = len(A)
    for index in xrange(0, lenA, 2):
        if index == lenA-1 or A[index] != A[index + 1]:
            return A[index]
