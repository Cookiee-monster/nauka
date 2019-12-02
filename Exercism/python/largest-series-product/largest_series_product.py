def largest_product(series, size):
    list_of_digits = [int(x) for x in str(series)]
    largest_product = 0
    temp_product = 1
    if series == "" and size > 0:
        raise ValueError("Series cannot be empty")
    if size > len(series):
        raise ValueError("Size cannot be larger than series")
    if size < 0:
        raise ValueError("Size cannot be smaller than 0")

    for iter in range(0, len(list_of_digits) - size + 1):
        for product in (list_of_digits[iter: iter + size]):
            temp_product *= product
        if temp_product > largest_product:
            largest_product = temp_product
        temp_product = 1
    return largest_product
