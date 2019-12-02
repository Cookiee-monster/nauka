import re

def translate(text):
    list_of_words = text.split()
    result = []
    for word in list_of_words:
        word = str(word)
        if re.match("^([a,e,i,o,u]\w+)|^(xr\w+)|^(yt\w+)", word):
            word += "ay"
        else:
            if re.match("^(qu)(\w+)", word):
                word = re.sub("^(qu)(\w+)", r"\2\1ay", word)
            elif re.match("^([^a,e,i,o,u]qu)(\w+)", word):
                word = re.sub("^([^a,e,i,o,u]qu)(\w+)", r"\2\1ay", word)
            elif re.match("^([^a,e,i,o,u]+)(y\w+)|^([^a,e,i,o,u])(y\w+)", word):
                word = re.sub("^([^a,e,i,o,u]+)(y\w+)|", r"\2\1ay", word)
            else:
                word = re.sub("^([^a,e,i,o,u]+)(\w+)|", r"\2\1ay", word)
        result.append(word)

    return " ".join(result)
