import re


class Phone(object):
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.pattern_11 = "\+?1 ?\(?([2-9][0-9]{2})\)?(?:[- \.\\\*]*)([2-9][0-9]{2})(?:[- \.\\\*]*)([0-9]{4})"
        self.pattern_10 = "\(?([2-9][0-9]{2})\)?(?:[- \.\\\*]*)([2-9][0-9]{2})(?:[- \.\\\*]*)([0-9]{4})"
        self.number = ""
        self.number_of_digits = len(re.findall("\d", phone_number))

        if self.number_of_digits == 10:
            if len(re.findall(self.pattern_10, phone_number)) == 0:
                raise ValueError(".")
            else:
                self.find_all = re.findall(self.pattern_10, phone_number)
        elif self.number_of_digits == 11:
            if len(re.findall(self.pattern_11, phone_number)) == 0:
                raise ValueError(".")
            else:
                self.find_all = re.findall(self.pattern_11, phone_number)
        else:
            raise ValueError(".")

        self.area_code = self.find_all[0][0]
        for element in self.find_all:
            self.number = "".join(element)


    def pretty(self):
        return "({}) {}-{}".format(self.area_code, self.find_all[0][1], self.find_all[0][2])
