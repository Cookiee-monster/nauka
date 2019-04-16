#! Python 3
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


def printing(number, result):
    return print("The factorial of the {} number is {}".
                 format(number, result))


def factorial(number):

    """
    :param number:      Input number which will be computed
    :return:    factorial value of the given number
    """
    result = 1
    if number == 0:
        result = 0
        return printing(number, result)
    if number == 1:
        result = 1
        return printing(number, result)
    else:
        for i in range(1, number + 1):
            result = result * i
        return printing(number, result)


factorial(8)

