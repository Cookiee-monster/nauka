def square(number):
    if number in range(1, 65):
        return 2 ** (number - 1)
    elif number <= 0:
        raise ValueError("Number cannot be 0 or negative")
    elif number > 64:
        raise ValueError("Number has to smaller or equal to 64")


def total(number):
    if number <= 0:
        raise ValueError("Number cannot be 0 or negative")
    elif number > 64:
        raise ValueError("Number has to smaller or equal to 64")
    elif number > 2:
        return sum([square(x) for x in range(1, number + 1)])
    elif number == 2:
        return 3
    elif number == 1:
        return 1

