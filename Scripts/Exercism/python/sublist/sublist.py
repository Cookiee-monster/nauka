"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "List a are a sublist of a list b."
SUPERLIST = "List a is a superlist of a list b"
EQUAL = "Those lists are equal"
UNEQUAL = "Those lists aren't equal"


def sublist(list_a, list_b):
    if list_a == list_b:
        return EQUAL

    if len(list_a) == 0:
        return SUBLIST
    elif len(list_b) == 0:
        return SUPERLIST

    if len(list_a) < len(list_b):
        for index in range(0, len(list_b) - len(list_a) + 1):
            if list_b[index: index + len(list_a)] == list_a:
                return SUBLIST

    elif len(list_b) < len(list_a):
        for index in range(0, len(list_a) - len(list_b) + 1):
            if list_a[index: index + len(list_b)] == list_b:
                return SUPERLIST

    if list_a != list_b:
        return UNEQUAL
