def is_palindrome(word):
    list_word = []
    backwards_word = ""
    for i in word:
        list_word.append(i.casefold())
    backwards_word = backwards_word.join(list_word[::-1])
    return word.casefold() == backwards_word


print(is_palindrome('Deleveled'))
print(is_palindrome('dupa'))
print(is_palindrome('kajak'))