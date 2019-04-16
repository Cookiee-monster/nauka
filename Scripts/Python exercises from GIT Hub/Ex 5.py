#! Python 3
# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class StringClass():
    def getString(self):
        self.text = input("Please input the desired text")

    def printString(self):
        print(self.text.upper())

tekst = StringClass()
tekst.getString()

tekst.printString()