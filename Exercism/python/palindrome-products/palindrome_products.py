def largest(min_factor, max_factor):

    if min_factor > max_factor:
        raise ValueError("Min factor cannot be bigger than max factor")

    list_of_palindromes, list_of_values = palindromes(min_factor, max_factor)

    if len(list_of_values) == 0:
        return None, []

    all_factors_pairs = [palindrome[1] for palindrome in list_of_palindromes if palindrome[0]
                         == max(list_of_values)]

    return max(list_of_values), uniqe_factor_pairs(all_factors_pairs)


def smallest(min_factor, max_factor):

    if min_factor > max_factor:
        raise ValueError("Min factor cannot be bigger than max factor")

    list_of_palindromes, list_of_values = palindromes(min_factor, max_factor)

    if len(list_of_values) == 0:
        return None, []

    all_factors_pairs = [palindrome[1] for palindrome in list_of_palindromes if palindrome[0]
                         == min(list_of_values)]

    return min(list_of_values), uniqe_factor_pairs(all_factors_pairs)


def palindromes(min_factor, max_factor):
    list_of_palindromes = [(x * y, sorted([x, y])) for x in range(min_factor, max_factor+1)
                           for y in range(min_factor, max_factor+1) if str(x * y) == str(reverse(x * y))]
    list_of_values = [x[0] for x in list_of_palindromes]

    return list_of_palindromes, list_of_values


def reverse(number):
    object_as_list = [x for x in str(number)]
    return "".join(reversed(object_as_list))


def uniqe_factor_pairs(all_pairs):
    final_factors_pairs = []
    for factor in all_pairs:
        if factor not in final_factors_pairs:
            final_factors_pairs.append(factor)

    return final_factors_pairs
