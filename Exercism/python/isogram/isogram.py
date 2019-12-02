def is_isogram(string):
    all_letters = []

    for letter in string:
        if letter.isalpha():
            all_letters.append(letter.lower())

    all_letters_set = set(all_letters)

    if len(all_letters) == len(all_letters_set):
        return True
    else:
        return False
