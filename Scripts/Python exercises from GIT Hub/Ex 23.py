#! Python 3
# Question:
#     Write a method which can calculate square value of number

class Square():
    def __init__(self, number):
        self.number = number

    def square_calc(self):
        self.square = self.number ** 2
        print("Square of {} number is {}".format(self.number, self.square))

value = int(input("Input the number:"))
potega = Square(value).square_calc()



