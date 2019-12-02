scores_dict = {}
temp_list = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
for letter in temp_list:
    scores_dict[letter] = 1

temp_list = ["D", "G"]
for letter in temp_list:
    scores_dict[letter] = 2

temp_list = ["B", "C", "M", "P"]
for letter in temp_list:
    scores_dict[letter] = 3

temp_list = ["F", "H", "V", "W", "Y"]
for letter in temp_list:
    scores_dict[letter] = 4

scores_dict["K"] = 5
scores_dict["J"] = scores_dict["X"] = 8
scores_dict["Q"] = scores_dict["Z"] = 10


def score(word):
    result = 0
    for letter in word:
        result += scores_dict.get(letter.upper(), 0)
    return result