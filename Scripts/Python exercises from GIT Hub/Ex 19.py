#! Python 3
# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
# age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

users_list = []

raw_input = input("Input the name of user, their age and score in the pattern Name,Age,Score:  ")
while raw_input:
    users_list.append(tuple(raw_input.split(",")))
    raw_input = input("Input the name of user, their age and score in the pattern Name,Age,Score:  ")

def sort_score(item):
    return item[2]

def sort_age(item):
    return item[1]

def sort_name(item):
    return item[0]

users_list.sort(key=sort_score)
users_list.sort(key=sort_age)
users_list.sort(key=sort_name)

print(users_list)

