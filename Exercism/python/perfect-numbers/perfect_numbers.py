def classify(number):

    if number <= 0:
        raise ValueError("Number cannot be 0 or negative.")

    divisors = [div for div in range(1, number) if number % div == 0]

    if sum(divisors) == number:
        return "perfect"

    elif sum(divisors) > number:
        return "abundant"

    else:
        return "deficient"
