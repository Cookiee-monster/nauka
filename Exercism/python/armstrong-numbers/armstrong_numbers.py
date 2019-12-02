def is_armstrong_number(number):
    number_as_str = str(number)
    result = 0

    for digit in number_as_str:
        result += int(digit) ** len(number_as_str)

    if result == number:
        return True
    else:
        return False
