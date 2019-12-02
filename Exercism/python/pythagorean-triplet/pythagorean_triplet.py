import math


def triplets_with_sum(number):
    result = []
    r_start = math.sqrt(number)
    if r_start is not int:
        r_start = math.floor(r_start)
        if r_start % 2 != 0:
            r_start -= 1
    for r in range(r_start, int(number/3), 2):
        half_of_r_square = r ** 2 // 2
        for s in range(1, int(half_of_r_square)):
            if half_of_r_square % s == 0:
                t = int(half_of_r_square // s)
                temp_list = sorted([r+s, r+t, r+s+t])
                if sum(temp_list) == number:
                    result.append((temp_list[0], temp_list[1], temp_list[2]))

    return set(result)


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    pass
