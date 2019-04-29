def recite(start_verse, end_verse):
    days_list = ["first", "second", "third",
                 "fourth", "fifth", "sixth",
                 "seventh", "eighth", "ninth",
                 "tenth", "eleventh", "twelfth"]

    gifts_list = ['a Partridge in a Pear Tree', 'two Turtle Doves', 'three French Hens', 'four Calling Birds',
                  'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking',
                  'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']
    result = []

    for i in range(start_verse-1, end_verse):
        temp_result = []
        temp_result.append("On the {} day of Christmas my true love gave to me:".format(days_list[i]))
        gifts = []
        if i == 0:
            gifts.append("{}.".format(gifts_list[i]))
        else:
            for day in range(i, 0, -1):
                gifts.append("{},".format(gifts_list[day]))
            gifts.append("and {}.".format(gifts_list[0]))
        temp_result += gifts
        temp_result = " ".join(temp_result)
        result.append(temp_result)

    return result

