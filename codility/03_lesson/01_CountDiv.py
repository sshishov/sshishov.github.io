# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B, K):
    # write your code in Python 2.7
    count = 0
    if A == B:
        count += 1 if A % K == 0 else 0
    else:
        if A % K == 0:
            pass
        else:
            if A < K:
                A = K
            else:
                A += K - (A % K)
        if B % K == 0:
            B += K
        else:
            if B < K:
                B = A
            else:
                B += (K - B % K)
            
        count += (B - A) // K
    return count