def transpose(lines):
    lines = lines.split("\n")
    if len(lines) > 1:

        max_row = max([len(x) for x in lines])
        max_col = len(lines)
        result = [x for x in lines[0]]
        while len(result) != max_row:
            result.append(" ")

        for col in range(1, max_col):
            for row in range(0, max([len(x) for x in lines[col:]])):
                try:
                    result[row] += lines[col][row]
                except IndexError:
                    result[row] += " "

    else:
        result = [x for x in lines[0]]

    return "\n".join(result)