def flatten(iterable):
    result = []
    result = make_list_flat(iterable, result)
    return result

def make_list_flat(iterable, result):
    for element in iterable:
        if element.__class__ == list:
            make_list_flat(element, result)
        else:
            if element or element == 0:
                result.append(element)
            else:
                pass
    return result
