import string

A_TO_Z = [string.ascii_lowercase[x] for x in range(0, 26)]
Z_TO_A = [string.ascii_lowercase[x] for x in range(25, -1, -1)]

def encode(plain_text):
    result = ""
    i = 0
    letters_to_encode = [letter.lower() for letter in plain_text if letter.isalpha() or letter.isdigit()]
    for letter in letters_to_encode:
        if letter.isalpha():
            result += Z_TO_A[A_TO_Z.index(letter)]
            i += 1
        elif letter.isdigit():
            result += letter
            i += 1
        else:
            pass
        if i == 5 and len(letters_to_encode) > 5 and letters_to_encode.index(letter) < len(letters_to_encode) - 4:
            result += " "
            i = 0
    return result


def decode(ciphered_text):
    result = ""
    i = 0
    letters_to_decode = [letter for letter in ciphered_text if letter.isalpha() or letter.isdigit()]
    for letter in letters_to_decode:
        if letter.isalpha():
            result += A_TO_Z[Z_TO_A.index(letter)]
        elif letter.isdigit():
            result += letter
        else:
            pass
    return result
