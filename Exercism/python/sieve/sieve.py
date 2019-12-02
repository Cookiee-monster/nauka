def primes(limit):
    prime_list = list(range(2, limit + 1))
    for i in prime_list:
        prime = 2 * i
        while prime <= max(prime_list):
            try:
                prime_list.remove(prime)
            except:
                pass
            prime += i
    return prime_list
