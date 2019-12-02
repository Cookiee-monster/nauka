numbers_dict_0_99 = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

thousands_dict = {
    1: "thousand",
    2: "million",
    3: "billion"
}

def say(number):
    if number is not int:
        number = int(number)

    if number < 0:
        raise ValueError("Value cannot be negative")
    elif number > 999999999999:
        raise ValueError("Value is too large")
    if number in range(0, 1000):
        return number_0_999(number)
    else:
        separated = split_into_thousands(number)
        result = []
        i = 0
        while len(separated) > 0:
            part_of_number = int(separated.pop())
            if i > 0:
                if part_of_number != 0:
                    result.append(number_0_999(int(part_of_number)) + " {}".format(thousands_dict[i]))
                    i += 1
                else:
                    i += 1
            else:
                if part_of_number != 0:
                    result.append(number_0_999(int(part_of_number)))
                    i += 1
                else:
                    i += 1
        result.reverse()
        return " ".join(result)

def number_0_999(number):
    if number in numbers_dict_0_99.keys():
        return numbers_dict_0_99[number]
    elif number in range(0, 99):
        tens = int(str(number)[-2]) * 10
        unit = int(str(number)[-1])
        return "{}-{}".format(numbers_dict_0_99[tens], numbers_dict_0_99[unit])
    elif number in range(100,1000):
        hundreds = int(str(number)[-3])
        if number % 100 == 0:
            return str(numbers_dict_0_99[hundreds]) + " hundred"
        else:
            tens = int(str(number)[-2]) * 10
            unit = int(str(number)[-1])
            return str(numbers_dict_0_99[hundreds]) + " hundred and " \
                   + (numbers_dict_0_99[tens]) + "-" + str(numbers_dict_0_99[unit])

def split_into_thousands(number):
    import re

    separated = []
    split_temp = re.split("(\d\d\d)$", str(number))
    separated.append(split_temp[1])
    while len(split_temp[0]) > 3:
        split_temp = re.split("(\d\d\d)$", split_temp[0])
        separated.append(split_temp[1])
    separated.append(split_temp[0])
    separated.reverse()
    return separated
