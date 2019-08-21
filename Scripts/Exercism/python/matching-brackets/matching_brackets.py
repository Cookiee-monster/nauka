import re


def is_paired(phrase):

    brackets_pattern = "(\[|\]|\{|\}|\(|\))"

    every_bracket = re.findall(brackets_pattern, phrase)
    
    if len(every_bracket) == 0:
        return True

    brackets_pairs = {
        "[": "]",
        "(": ")",
        "{": "}"}

    bracket_type = {
        "[": "opening",
        "(": "opening",
        "{": "opening",
        "]": "closing",
        ")": "closing",
        "}": "closing"}

    open_brackets = []
    index = 0
        
    while len(every_bracket) > 0:
        current_bracket = every_bracket.pop(0)
        if bracket_type[current_bracket] == "opening":
            open_brackets.append((current_bracket, index))
        elif bracket_type[current_bracket] == "closing":
            current_bracket = (current_bracket, index)
            if len(open_brackets) > 0:
                currently_open = open_brackets.pop()
                if brackets_pairs[currently_open[0]] != current_bracket[0] or currently_open[1] \
                        > current_bracket[1]:
                    return False
            else:
                return False
        index += 1

    if len(open_brackets) > 0:
        return False
    else:
        return True
