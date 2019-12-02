import re

def verify(isbn):
    isbn_as_a_list = re.findall("([0-9X])", isbn)
    if len(isbn_as_a_list) != 10:
        return False
    result = 0
    multiplier = 10
    for digit in isbn_as_a_list:
        if digit.isdigit():
            result += int(digit) * multiplier
        elif digit == "X" and multiplier == 1:
            result += 10 * multiplier
        else:
            return False
        multiplier -= 1
    if result % 11 == 0:
        return True
    else:
        return False
