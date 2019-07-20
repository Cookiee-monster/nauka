import math


def cipher_text(plain_text):
    to_encode = ""
    for char in plain_text:
        if char.isalpha():
            to_encode += char.lower()
        elif char.isdigit():
            to_encode += char
        else:
            continue

    if len(to_encode) == 0:
        return plain_text

    to_encode_len = math.sqrt(len(to_encode))
    if to_encode_len is int:
        columns = rows = int(to_encode_len)
        square_text_list = [to_encode[i:i + columns] for i in range(0, columns ** 2, columns)]
    else:
        columns = math.ceil(to_encode_len)
        if columns * math.floor(to_encode_len) >= len(to_encode):
            rows = math.floor(to_encode_len)
        else:
            rows = columns
        while len(to_encode) != columns * rows:
            to_encode += " "

        square_text_list = [to_encode[i:i + columns] for i in range(0, int(columns * rows), int(columns))]

    chunk_of_result = ""
    result_chunks_list = []
    result = ""
    for col in range(0, columns):
        for row in square_text_list:
            if row[col] != " ":
                chunk_of_result += row[col]
        while len(chunk_of_result) != rows:
            chunk_of_result += " "
        result_chunks_list.append(chunk_of_result)
        chunk_of_result = ""
    # result = " ".join([result_as_string[i: i + int(columns - 1)] for i in range(0, int(columns * (columns - 1)),
    #                                                                             int(columns - 1))])
    result = " ".join(result_chunks_list)
    return result
