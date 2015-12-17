# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    lenA = len(A)
    total = sum(A)
    leftsum = A[0]
    small_total = None
    for index in range(1, lenA):
        possible_small_total = abs(total - leftsum - leftsum)
        if small_total is None or small_total > possible_small_total:
            small_total = possible_small_total
        leftsum += A[index]
    return small_total
