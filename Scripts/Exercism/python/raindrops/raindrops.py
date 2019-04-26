def raindrops(number):
    a = b = c = ""
    if number % 3 == 0:
        a = "Pling"
    if number % 5 == 0:
        b = "Plang"
    if number % 7 == 0:
        c = "Plong"

    if a or b or c:
        output = a+b+c
    else:
        output = str(number)
    return output