def roman(number):
    roman_dict = {
        4: "IV",
        5: "V",
        9: "IX"
    }

    result = ""
    if number >= 1000:
        result += "M" * (number//1000)
        number -= 1000 * (number//1000)

    if number >= 900:
        result += "CM"
        number -= 900

    if number in range(500, 900):
        result += "D" * (number//500)
        number -= 500 * (number//500)

    if number >= 400:
        result += "CD"
        number -= 400

    if number in range(100, 400):
        result += "C" * (number//100)
        number -= 100 * (number//100)

    if number >= 90:
        result += "XC"
        number -= 90

    if number >= 50:
        result += "L"
        number -= 50

    if number >= 40:
        result += "XL"
        number -= 40

    if number in range(10, 40):
        result += "X" * (number//10)
        number -= 10 * (number//10)

    if number in [4, 5, 9]:
        result += roman_dict[number]
        return result

    if number > 5:
        result += "V" + "I" * (number % 5)
        return result

    if number <= 3:
        result += "I" * (number//1)
        return result
