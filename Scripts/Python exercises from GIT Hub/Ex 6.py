#! Python 3
# Question 6
# Level 2
#
# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math

# Constants:
C = 50
H = 30


def required_formula(d, c = C, h = H):
    """

    :param d: the input parameter
    :param c: constant value C
    :param h: constant value H
    :return: The result of the formula  Q = Square root of [(2 * C * D)/H]
    """

    return math.sqrt(2*c*d/h)

numbers_input = input("Input numbers for calculation using comma separator")
list_of_number = numbers_input.split(",")
results = []
for number in list_of_number:
    d = int(number)
    results.append(required_formula(d))

for result in results:
    print(str(result) + ",", end = "")


