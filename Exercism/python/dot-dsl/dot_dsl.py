NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if data:
            for entry in data:
                if type(entry) is not tuple or len(entry) == 0:
                    raise TypeError("Data should be provided as a list of tuples")

                if entry[0] == NODE:
                    if len(entry) == 3:
                        try:
                            node = Node(*entry[1:3])
                            self.nodes.append(node)
                        except TypeError:
                            raise TypeError("Type of arguments if wrong")
                    else:
                        raise ValueError("Wrong number of arguments")

                elif entry[0] == EDGE:
                    if len(entry) == 4:
                        try:
                            edge = Edge(*entry[1:4])
                            self.edges.append(edge)
                        except TypeError:
                            raise TypeError("Type of arguments if wrong")
                    else:
                        raise ValueError("Wrong number of arguments")

                elif entry[0] == ATTR:
                    if len(entry) <= 3:
                        try:
                            self.attrs.update({entry[1]: entry[2]})
                        except IndexError:
                            raise TypeError("Type of arguments if wrong")
                    else:
                        raise ValueError("Wrong number of arguments")

                else:
                    raise ValueError("Unknown item")
