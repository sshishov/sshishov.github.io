# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    max = 0
    count = 0
    for item in bin(N)[2:]:
        if item == '1':
            if count > max:
                max = count
            count = 0
        else:
            count += 1
    return max