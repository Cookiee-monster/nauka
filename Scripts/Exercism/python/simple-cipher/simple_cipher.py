import string
from itertools import cycle
import random


class Cipher(object):
    def __init__(self, key=None):
        self.a_to_z = [string.ascii_lowercase[x] for x in range(0, 26)]
        self.key = key
        self.key_as_numbers = []
        self.result = ""
        if self.key:
            self.key_as_numbers = [self.a_to_z.index(char.lower()) for char in self.key if char.isalpha()]
        else:
            i = 1
            self.key = ""
            while i < 100:
                self.key += random.choice(self.a_to_z)
                i += 1
            self.key_as_numbers = [self.a_to_z.index(char.lower()) for char in self.key if char.isalpha()]

    def encode(self, text):
        self.result = ""
        self.to_encode = list(zip([letter for letter in text], cycle(self.key_as_numbers)))
        self.result = self.rotate(1)
        return self.result

    def decode(self, text):
        self.result = ""
        self.to_decode = list(zip([letter for letter in text], cycle(self.key_as_numbers)))
        self.result = self.rotate(-1)
        return self.result

    def rotate(self, direction):
        if direction == 1:
            to_translate = self.to_encode
        else:
            to_translate = self.to_decode

        for pair in to_translate:
            char = pair[0]
            if char.isalpha():
                rotator = pair[1] * direction
                if char.islower():
                    self.result += self.a_to_z[(self.a_to_z.index(char) + rotator) % 26]
                else:
                    self.result += self.a_to_z[(self.a_to_z.index(char.lower()) + rotator) % 26].upper()
            else:
                self.result += char
        return self.result
