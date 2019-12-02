def saddle_points(matrix):

    # First condition check - if matrix is not an empty one
    if len(matrix) == 0 or matrix[0] == 0:
        return [{}]

    # Second check for irregular matrix
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("The matrix is irregular")

    matrix_dict = translate_matrix_to_dict(matrix)  # translation to dict format matrix
    transposed_matrix = transpose_matrix(matrix)    # matrix transposition
    transposed_matrix_dict = transpose_matrix(matrix_dict)  # dict format matrix transposition

    candidates_in_rows = []  # list for possible candidates found in rows
    row_index = 0  # index of the currently analysed row
    for row_dict in matrix_dict:
        candidates_in_rows += [candidate for candidate in row_dict if candidate["element"]
                               == max(matrix[row_index])]
        row_index += 1

    candidates_in_col = []
    col_index = 0
    for col_dict in transposed_matrix_dict:
        candidates_in_col += [candidate for candidate in col_dict if candidate["element"]

                              == min(transposed_matrix[col_index])]
        col_index += 1

    result = [{"row": candidate_max["row"]+1, "column": candidate_max["column"]+1} for candidate_max
              in candidates_in_rows if candidate_max in candidates_in_col]

    if len(result) > 0:
        return result
    else:
        return [dict()]


# Function which translate the matrix to represent each cell as a dict
def translate_matrix_to_dict(matrix):
    matrix_of_dict = []
    for i in range(0, len(matrix)):
        matrix_of_dict.append([])

    row_index = 0
    col_index = 0
    for row in matrix:
        for element in row:
            matrix_of_dict[row_index].append(
                {
                 "element":  element,  # value of a cell
                 "row": row_index,  # row of the cell
                 "column": col_index  # column of the cell
                }
            )
            col_index += 1
        row_index += 1
        col_index = 0
    return matrix_of_dict


# Function which transpose the matrix
def transpose_matrix(matrix):
    transposed_matrix = []
    for i in range(0, len(matrix[0])):
        transposed_matrix.append([])

    for row in matrix:
        i = 0
        for element in row:
            transposed_matrix[i].append(element)
            i += 1

    return transposed_matrix
