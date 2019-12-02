def recite(start, take=1):

    current_beer = start
    result = []
    while take != 0:
        if current_beer > 2:
            result += \
                ["{0} bottles of beer on the wall, {0} bottles of beer.".format(str(current_beer)),
                "Take one down and pass it around, {} bottles of beer on the wall.".format(str(current_beer - 1)),
                ]
            if take > 1:
                result += [""]

        elif current_beer == 2:
            result += \
                ["2 bottles of beer on the wall, 2 bottles of beer.",
                 "Take one down and pass it around, 1 bottle of beer on the wall."
                 ]
            if take > 1:
                result += [""]

        elif current_beer == 1:
            result += \
                ["1 bottle of beer on the wall, 1 bottle of beer.",
                "Take it down and pass it around, no more bottles of beer on the wall."
                ]
            if take > 1:
                result += [""]
        else:
            result += \
                [
                "No more bottles of beer on the wall, no more bottles of beer.",
                "Go to the store and buy some more, 99 bottles of beer on the wall."
                ]
        take -= 1
        current_beer -= 1

    return result
