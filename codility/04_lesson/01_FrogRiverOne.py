# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7
    lenA = len(A)
    B = [None] * X
    for index in range(lenA):
        if B[A[index] - 1] is None:
            B[A[index] - 1] = index
    if None not in B:
        return max(B)
    return -1
