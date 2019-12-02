def annotate(minefield):

    if len(minefield) == 0:
        return minefield

    for row in minefield:
        for char in row:
            if char not in [" ", "*"]:
                raise ValueError("Wrong character")

    list_of_columns = [len(row) for row in minefield]

    if min(list_of_columns) == max(list_of_columns):
        last_column = list_of_columns[0] - 1
    else:
        raise ValueError("The minefield is not a rectangle")

    last_row = len(minefield) - 1
    result_minefield = minefield[:]

    for current_row in range(0, last_row + 1):
        for current_col in range(0, last_column + 1):
            if minefield[current_row][current_col] != "*":
                counter = count_mines(minefield, current_row, current_col)
                result_minefield[current_row] = result_minefield[current_row][:current_col] \
                                                + counter + result_minefield[current_row][current_col+1:]

    return result_minefield


def count_mines(minefield, current_row, current_col):
    mines_counter = 0
    for row in range(current_row - 1, current_row + 2):
        for col in range(current_col - 1, current_col + 2):
            if col >= 0 and row >= 0:
                try:
                    if minefield[row][col] == "*":
                        mines_counter += 1
                except :
                    continue
    if mines_counter > 0:
        return str(mines_counter)
    else:
        return " "
