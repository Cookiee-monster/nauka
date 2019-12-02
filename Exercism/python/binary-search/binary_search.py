import math


def find(search_list, value):

    if any((max(search_list) < value, min(search_list) > value)):
        raise ValueError("Value is not on the list")

    working_search_list = search_list[:]

    i = step = max_numb_of_iterations = math.floor(len(search_list) / 2)
    iteration = 0
    while iteration <= max_numb_of_iterations:
        if search_list[i] == value:
            return i
        elif search_list[i] > value:
            working_search_list = working_search_list[:step]
            step = math.ceil(len(working_search_list) / 2)
            i -= step
            iteration += 1
        else:
            working_search_list = working_search_list[step:]
            step = math.ceil(len(working_search_list) / 2)
            i += step
            iteration += 1

    raise ValueError("Value cannot be found")


