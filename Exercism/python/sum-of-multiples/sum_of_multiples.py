def sum_of_multiples(limit, multiples):
    result = []
    for multiplier in multiples:
        if multiplier > 0:
            result += [x for x in range(1, limit) if x % multiplier == 0]
        else:
            pass
    return sum(set(result))
