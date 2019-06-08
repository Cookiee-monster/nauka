def encode(string):
    if len(string) == 0:
        return string
    current_char = string[0]
    counter = 1
    result = ""
    for char in string[1:]:
        if char == current_char:
            counter += 1
        else:
            if counter > 1:
                result += str(counter)
            result += str(current_char)
            counter = 1
            current_char = char
    if counter > 1:
        result += str(counter)
    result += str(current_char)
    return result


def decode(string):
    result = ""
    multiplier = ""
    for elem in range(0, len(string)):
        if string[elem].isdigit():
            multiplier += str(string[elem])
        else:
            try:
                if int(multiplier) > 0:
                    result += string[elem] * int(multiplier)
                    multiplier = ""
            except:
                    result += string[elem]

    return result
