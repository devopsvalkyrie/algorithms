from collections import deque
from random import randint


def max_min_of_given_length_subarray(array, length):
    maximum = min(array[:length])
    d = deque()
    d.append(0)

    for i in range(len(array)):
        if i - d[0] == length:
            d.popleft()
        while len(d) and array[d[-1]] >= array[i]:
            d.pop()
        d.append(i)
        if i >= length:
            maximum = max(maximum, array[d[0]])

    return maximum


if __name__ == '__main__':

    array = []
    for i in range(20):
        array.append(randint(1, 100))
    print(array)

    length = 3

    maximum_of_min = max_min_of_given_length_subarray(array=array, length=length)
    print(maximum_of_min)
