def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError ("Strand's lenghts are not the same")

    distance_result = 0
    for i in range(0, len(strand_a)):
        if strand_a[i] != strand_b[i]:
            distance_result += 1

    return distance_result






