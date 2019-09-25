from itertools import combinations as comb


def check_coordinates(sublist, graph):
    coord1, coord2, coord3, coord4 = sublist
    if all((coord1[1] == coord2[1], coord1[0] == coord3[0], coord2[0] == coord4[0], coord3[1] == coord4[1])):
        x = coord1[0]
        y = coord1[1]
        width = coord2[0] - coord1[0]
        height = coord4[1] - coord2[1]

        graph_bite_ver = [row[x] for row in graph[y:y + height]] + [row[x + width] for row in graph[y:y + height]]
        graph_bite_hor = graph[y][x:x + width] + graph[y + height][x:x + width]
        for char in graph_bite_ver:
            if char not in ["+", "|"]:
                return False

        for char in graph_bite_hor:
            if char not in ["+", "-"]:
                return False

        return True
    else:
        return False


def rectangles(strings):

    list_of_corners = [(x, y) for y in range(len(strings)) for x in range(len(strings[y]))
                       if strings[y][x] == "+"]
    list_of_corners_combinations = [sorted(list(combin), key=lambda keys: (combin[1], combin[2]), reverse=True)
                                    for combin in list(comb(list_of_corners, 4))]

    list_of_rectangles = [sublist for sublist in list_of_corners_combinations if check_coordinates(sublist, strings)]

    return len(list_of_rectangles)
