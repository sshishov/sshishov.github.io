# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

from collections import defaultdict

def solution(N, A):
    # write your code in Python 2.7
    max_value = 0
    prev_pos = 0
    max_list = [index for (index, value) in enumerate(A) if value == N + 1]
    for index in max_list:
        count_dict = defaultdict(lambda: max_value)
        for item in A[prev_pos:index]:
            count_dict[item] += 1
        values = count_dict.values()
        if values:
            max_value = max(values)
        prev_pos = index + 1
    result = [max_value] * N
    for item in A[prev_pos:]:
        result[item - 1] += 1
    return result