def factors(value):
    if value > 1:
        divisors = []
        for div in range(2, value + 1):
            if check_if_prime(div):
                while value % div == 0:
                    divisors.append(div)
                    value /= div
                    if int(value) == 1:
                        return divisors
    elif value == 1:
        return []
    elif value <= 0:
        raise ValueError("Value has to be bigger than 0")


def check_if_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for x in range(2, number):
            if number % x == 0:
                return False
            else:
                return True
