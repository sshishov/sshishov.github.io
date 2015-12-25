# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, Y, D):
    # write your code in Python 2.7
    return (Y - X) // D + 1 if (Y - X) % D else (Y - X) / D
