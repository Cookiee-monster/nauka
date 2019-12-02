def append(list1, list2):
    list1 += list2
    return list1


def concat(lists):
    result = []
    for item in lists:
        result += item

    if list in result:
        return concat(result)
    else:
        return result


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    i = 0
    for item in list:
        if item:
            i += 1
    return i


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):

    if length(list) == 0:
        return initial

    result = function(initial, list[0])
    if length(list) > 1:
        for item in list[1:]:
            result = function(result, item)
        return result
    else:
        return result


def foldr(function, list, initial):
    if length(list) == 0:
        return initial

    list = reverse(list)
    result = function(list[0], initial)
    if length(list) > 1:
        for item in list[1:]:
            result = function(item, result)
        return result
    else:
        return result


def reverse(list):
    return [x for x in list[-1:-len(list)-1:-1]]