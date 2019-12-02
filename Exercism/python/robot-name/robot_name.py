import random
import string


class Robot(object):
    def __init__(self):
        self.letters = [string.ascii_uppercase[x] for x in range(0, 26)]
        self.name = self.give_name()

    def reset(self):
        self.name = self.give_name()
        return self.name

    def give_name(self):
        self.name = ""
        random.seed()
        while len(self.name) != 2:
            self.name += random.choice(self.letters)
        while len(self.name) != 5:
            self.name += str(random.randint(0, 9))

        return self.name