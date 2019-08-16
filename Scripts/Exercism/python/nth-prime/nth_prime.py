import math


def prime(number):
    list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    if number == 0:
        raise ValueError("Number can not be 0")

    if number <= len(list_of_primes):
        return list_of_primes[number - 1]

    else:
        candidate = list_of_primes[-1] + 1
        while len(list_of_primes) != number:
            if candidate % 2 != 0:
                if is_a_prime(candidate):
                    list_of_primes.append(candidate)
                    print(list_of_primes.index(candidate))
            candidate += 1
        return list_of_primes[-1]


def is_a_prime(specific_number):
    temp_list = []

    for div in range(1, round(math.sqrt(specific_number)) + 1):
        if specific_number % div == 0:
            temp_list.append(div)
            if len(temp_list) > 1:
                return False
    return True
