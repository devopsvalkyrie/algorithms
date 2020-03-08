def check_zeros(number):
    number_of_zeros = 0
    while number:
        number_of_zeros += number // 5
        number //= 5

    return number_of_zeros


def factorial_search(number_of_zeros):

    left = 0
    right = number_of_zeros * 5
    while left < right:
        middle = (left + right) // 2

        if check_zeros(middle) < number_of_zeros:
            left = middle + 1
        else:
            right = middle

    if check_zeros(left) == number_of_zeros:
        return left
    return None


if __name__ == '__main__':

    for i in range(101):
        print(i, factorial_search(number_of_zeros=i))
