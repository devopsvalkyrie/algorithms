def max_sum_subarray(array):

    array_length = len(array)
    max_sum = array[0]
    current_sum = array[0]
    for item in range(1, array_length):
        current_sum = max(current_sum + array[item], array[item])
        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == '__main__':

    array = [1, 2, 3, -7, 12, 1]
    max_sum = max_sum_subarray(array=array)
    print(max_sum)
