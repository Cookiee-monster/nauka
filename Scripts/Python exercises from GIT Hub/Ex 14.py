#! Python 3
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

raw_input = input("Pass the string You'd like to analyse: ")

s = raw_input
result = {"UPPER CASE": 0, "LOWER CASE" : 0}
for c in s:
    if c.isupper():
        result["UPPER CASE"] += 1
    elif c.islower():
        result["LOWER CASE"] += 1
    else:
        pass


print("UPPER CASE: " + str(result["UPPER CASE"]))
print("LOWER CASE: " + str(result["LOWER CASE"]))