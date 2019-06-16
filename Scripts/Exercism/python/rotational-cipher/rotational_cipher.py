import string

a_to_z = [string.ascii_lowercase[x] for x in range(0, 26)]


def key_modulo(key):
    if key >= 26:
        key %= 26
        return key
    else:
        return key


def rotate(text, key):
    key = key_modulo(key)
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += a_to_z[(a_to_z.index(char) + key) % 26]
            else:
                result += a_to_z[(a_to_z.index(char.lower()) + key) % 26].upper()
        else:
            result += char

    return result
