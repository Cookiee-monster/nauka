#! Python 3
# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4
# digit binary numbers as its input and then check whether they are
# divisible by 5 or not. The numbers that are divisible by 5 are
# to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

binary_numbers = input("Enter binary values separated by comma:   ")
binary_numbers_list = binary_numbers.split(",")
divided_by_five = []
for number in binary_numbers_list:
    if int(number, 2) % 5 == 0:
        divided_by_five.append(number)

print(",".join(divided_by_five))