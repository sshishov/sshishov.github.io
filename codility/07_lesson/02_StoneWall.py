# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(H):
    # write your code in Python 2.7
    array = []
    count = 0
    for item in H:
        if array:
            if item > array[-1]:
                array.append(item)
                count += 1
            else:
                while (array and item < array[-1]):
                    array.pop()
                if not array or array[-1] != item:
                    array.append(item)
                    count += 1
        else:
            array.append(item)
            count += 1
    return count