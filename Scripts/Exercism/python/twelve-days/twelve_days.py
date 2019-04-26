def recite(start_verse, end_verse):
    days_list = ["first", "second", "third",
                 "fourth", "fifth", "sixth",
                 "seventh", "eighth", "ninth",
                 "tenth", "eleventh", "twelfth"]

    gifts_list = ["twelve Drummers Drumming", "eleven Pipers Piping", "ten Lords-a-Leaping", "nine Ladies Dancing",
                  "eight Maids-a-Milking", "seven Swans-a-Swimming", "six Geese-a-Laying", "five Gold Rings",
                  "four Calling Birds", "three French Hens", "two Turtle Doves", "a Partridge in a Pear Tree"]
    number_of_verses = end_verse - start_verse
    first_day = start_verse - 1
    result = ""
    if number_of_verses == 0:
        result = "On the {} day of Christmas my true love gave to me: \n".format(days_list[first_day])
        result += "{}, \n".format(gifts_list[-start_verse])
    else:
        for i in range(start_verse - 1, end_verse):
            gifts = str(gifts_list[-start_verse])
            if i != 0:
                for day in range(start_verse + 1, start_verse + i + 1):
                    if day != start_verse + i:
                        gifts += ", {}".format(gifts_list[-day])
                    else:
                        gifts += " and {}".format(gifts_list[-day])

            result += "On the {} day of Christmas my true love gave to me: {}.\n".format(days_list[i], gifts)
    print(result)
    return result

recite(1,1)