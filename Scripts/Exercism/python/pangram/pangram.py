def is_pangram(sentence):
    import re

    sentence_as_a_list = re.findall("([a-z])", sentence.lower())
    if len(set(sentence_as_a_list)) == 26:
        return True
    else:
        return False
