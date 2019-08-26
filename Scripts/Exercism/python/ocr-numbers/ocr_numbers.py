def convert(input_grid):
    list_of_tuples = each_char_as_a_tuple(input_grid)
    result = ""

    dict_bin_numbers = {
       (" _ ",
        "| |",
        "|_|"): "0",

        ("   ",
         "  |",
         "  |"): "1",

       (" _ ",
        " _|",
        "|_ ",): "2",

       (" _ ",
        " _|",
        " _|"): "3",

       ("   ",
        "|_|",
        "  |",): "4",

       (" _ ",
        "|_ ",
        " _|"): "5",

       (" _ ",
        "|_ ",
        "|_|"): "6",

        (" _ ",
         "  |",
         "  |"): "7",

        (" _ ",
         "|_|",
         "|_|"): "8",

        (" _ ",
         "|_|",
         " _|"): "9",

        "\n": ","
    }

    for digit_tuple in list_of_tuples:
        result += dict_bin_numbers.get(digit_tuple, "?")

    return result

def each_char_as_a_tuple(grid):
    if len(grid[0]) == len(grid[1]) == len(grid[2]):
        if len(grid[0]) % 3 != 0:
            raise ValueError(".")
        elif len(grid) % 4 != 0:
            raise ValueError(".")

        tuples_of_char = []
        for line in range(0, len(grid), 4):
            for char in range(0, len(grid[0]), 3):
                tuples_of_char.append((grid[line][char: char + 3],
                                       grid[line + 1][char: char + 3],
                                       grid[line + 2][char: char + 3]))
            if len(grid) > 4 and line < len(grid) - 4:
                tuples_of_char.append("\n")
        return tuples_of_char
    else:
        raise ValueError(".")




