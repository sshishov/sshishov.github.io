# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    lenA = len(A)
    if not lenA:
        return -1
    elif lenA == 1:
        return 0
    else:
        total = sum(A)
        leftsum = 0
        for index in range(lenA):
            if total - A[index] - leftsum == leftsum:
                return index
            leftsum += A[index]
    return -1
