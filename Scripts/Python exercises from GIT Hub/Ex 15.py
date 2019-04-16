#! Python 3
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

a = input("Input the digit a : ")
i = 1
result = 0
while i < 5:
    result += int(a*i)
    i += 1

print(result)