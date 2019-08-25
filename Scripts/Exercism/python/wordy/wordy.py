import re


def minus(a, b):
    return a - b


def plus(a, b):
    return a + b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def power(a, b):
    return a ** b



def pick_the_action(action, a, b):
    if action == "plus":
        return plus(a, b)
    elif action == "minus":
        return minus(a, b)
    elif action == "divided by":
        return divide(a, b)
    elif action == "multiplied by":
        return multiply(a, b)
    elif action == "raised to the":
        return power(a, b)


def answer(question):

    numbers_pattern = "(-?\d+)"
    action_pattern = "(plus|minus|divided by|multiplied by|raised to the)"
    detect_all_pattern = "(-?\d+|plus|minus|divided by|multiplied by|raised to the)"

    all_numbers = [int(element) for element in re.findall(numbers_pattern, question)]
    all_actions = re.findall(action_pattern, question)
    detect_all = re.findall(detect_all_pattern, question)

    if len(all_numbers) == 1 and len(all_actions) == 0:
        if re.search("(?:-?\d+) (.+[^?])", question):
            raise ValueError(".")
        else:
            return all_numbers[0]

    elif len(all_numbers) - 1 != len(all_actions):
        raise ValueError(".")

    elif len(all_numbers) == 0 or len(all_actions) == 0:
        raise ValueError(".")

    elif len(all_numbers) == 1 and len(all_actions) == 0:
        return all_numbers[0]

    else:
        result = 0
        action = all_actions.pop(0)
        a = int(detect_all.pop(0))

        try:
            action = detect_all.pop(0)
        except:
            raise ValueError(".")

        b = int(detect_all.pop(0))

        result += pick_the_action(action, a, b)
        while len(detect_all) != 0:
            try:
                action = detect_all.pop(0)
            except:
                raise ValueError(".")
            b = int(detect_all.pop(0))
            result = pick_the_action(action, result, b)

        return result
