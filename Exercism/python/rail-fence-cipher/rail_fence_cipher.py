def encode(message, rails):

    # Translate the message into the list
    message_as_list = [message[x] for x in range(0, len(message))]
    # Currently used rail
    rail = rails
    # Maximal possible indent (for 1st and last rail)
    max_indent = (rails - 1)*2
    result = ""

    # First row/rail - max indent between next characters
    while rail == rails:
        for char in range((rails-rail), len(message_as_list), max_indent):
            result += message_as_list[char]
        rail -= 1

    while rail != 1:
        # To reproduce the behaviour that for lower rails characters' indent is not equal
        indents = ((rail - 1)*2, max_indent - (rail - 1)*2)
        char = rails - rail
        result += message_as_list[char]  # First character from the row
        iteration = 1
        while char <= len(message_as_list):
            if iteration % 2 == 0:
                char += indents[1]
                iteration += 1
            else:
                char += indents[0]
                iteration += 1
            try:
                result += message_as_list[char]
            except:
                continue
        rail -= 1

    for char in range(rails-1, len(message_as_list), max_indent):
        result += message_as_list[char]
    return result


def decode(encoded_message, rails):
    # Encoded message into a list format
    message_as_list = [encoded_message[x] for x in range(0, len(encoded_message))]
    # Counted number of character which occures on each rail
    number_of_char_in_rail = []
    rail = rails
    max_indent = (rails - 1)*2
    result = ""
    # Counter of characters on rail
    count_char = 0

    # Count number of characters in each row
    while rail == rails:
        for char in range((rails-rail), len(message_as_list), max_indent):
            count_char += 1
        rail -= 1
        number_of_char_in_rail.append(count_char)
        count_char = 0

    while rail != 1:
        # To reproduce the behaviour that for lower rails characters' indent is not equal
        indents = ((rail - 1)*2, max_indent - (rail - 1)*2)
        char = rails - rail
        if char <= len(message_as_list):
            count_char += 1
            iteration = 1

        while char < len(message_as_list):
            if iteration % 2 == 0:
                char += indents[1]
                iteration += 1
                if char < len(message_as_list):
                    count_char += 1
            else:
                char += indents[0]
                iteration += 1
                if char < len(message_as_list):
                    count_char += 1
        number_of_char_in_rail.append(count_char)
        count_char = 0
        rail -= 1

    count_char = 0
    for char in range(rails-1, len(message_as_list), max_indent):
        if char <= len(message_as_list):
            count_char += 1
    number_of_char_in_rail.append(count_char)

    # To split the encoded message into chunks equal to number of char in each rail
    list_of_char_on_rail = []
    start = 0
    for number in number_of_char_in_rail:
        stop = start + number
        list_of_char_on_rail.append(message_as_list[start:stop])
        start += number

    # Get the proper character from each chunk (characters on a rail)
    result += list_of_char_on_rail[0].pop(0)
    current_char = 1
    direction = 'up'
    while current_char != len(message_as_list):
        # Popping characters from the highest rail to the lowest one
        if direction == 'up':
            for chunk in list_of_char_on_rail[1:]:
                try:
                    result += chunk.pop(0)
                except:
                    continue
                current_char = len(result)
            direction = 'down'

        # Popping characters in opposite direction
        elif direction == 'down':
            for chunk in reversed(list_of_char_on_rail[0:rails-1]):
                try:
                    result += chunk.pop(0)
                except:
                    continue
                current_char = len(result)
            direction = 'up'

    return result
