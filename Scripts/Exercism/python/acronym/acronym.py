def abbreviate(words):

    import re

    word_list = re.findall("[a-zA-Z0-9]+'*[a-zA-Z0-9]*", words)
    abbreviation = ""
    for word in word_list:
        abbreviation += word[0].upper()
    return abbreviation


