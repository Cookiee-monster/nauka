class Luhn(object):
    def __init__(self, card_num):
        import re

        self.card_num = card_num
        self.list_of_digits = [int(i) for i in re.findall("([0-9])", self.card_num)]
        self.list_of_all_element = re.findall("([^ ])", self.card_num)

    def is_valid(self):
        "check len of the number"
        if len(self.list_of_digits) <= 1:
            return False
        "check if num do not contain special characters despite whitespace"
        if len(self.list_of_digits) != len(self.list_of_all_element):
            return False
        "double every second digit"
        self.list_of_digits_to_test = self.list_of_digits[:]
        try:
            for i in range(-2, -len(self.list_of_digits_to_test)-1, -2):
                if self.list_of_digits_to_test[i] * 2 > 9:
                    self.list_of_digits_to_test[i] = self.list_of_digits_to_test[i] * 2 - 9
                else:
                    self.list_of_digits_to_test[i] = self.list_of_digits_to_test[i] * 2
        except:
            pass
        "check sum of digits"
        self.suma = sum(self.list_of_digits_to_test)
        if self.suma % 10 == 0:
            return True
        else:
            return False
luhn = Luhn("59")
print(luhn.is_valid())