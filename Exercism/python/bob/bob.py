import re


def response(hey_bob):

    if re.findall("([\?]$)|(\? +$)", hey_bob):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."

    if hey_bob.isupper():
        return "Whoa, chill out!"

    if len(re.findall("([\t\n\r ])", hey_bob)) == len(hey_bob):
        return "Fine. Be that way!"

    return "Whatever."
