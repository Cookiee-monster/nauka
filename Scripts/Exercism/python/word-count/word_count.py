def word_count(phrase):
    import re

    word_list = re.findall("[a-zA-Z0-9]+'*[a-zA-Z0-9]+|[a-zA-Z0-9]+", phrase)
    word_dic = {}

    for word in word_list:
        if word.lower() in word_dic.keys():
            word_dic[word.lower()] += 1
        else:
            word_dic[word.lower()] = 1

    return word_dic
print(word_count("Joe can't tell between 'large' and large."))
