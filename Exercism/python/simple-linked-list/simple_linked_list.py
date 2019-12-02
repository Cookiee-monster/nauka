class Node(object):
    def __init__(self, value):
        self.data = value
        self.nxt = None

    def value(self):
        return self.data

    def next(self):
        return self.nxt if self.nxt else None


class LinkedList(object):
    def __init__(self, values=[]):

        self.values = values
        self.counter = 0
        self.nodes = []
        self.head_elem = None


        for value in values:
            self.push(value)

        self.index = self.__len__() - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            result = self.nodes[self.index].value()
            self.index -= 1
            return result
        raise StopIteration

    def __len__(self):
        return self.counter

    def __getattr__(self, item):
        return self.values

    def head(self):
        if self.__len__() > 0:
            return self.head_elem
        else:
            raise EmptyListException("The linked list is empty")

    def push(self, value):
        new_node = Node(value)

        if self.__len__() >= 1:
            new_node.nxt = self.head()
        else:
            new_node.nxt = None
        self.head_elem = new_node
        self.counter += 1
        self.nodes.append(new_node)

    def pop(self):
        if self.__len__() == 0:
            raise EmptyListException("The linked list is empty")
        else:
            popped_node = self.head()
            self.head_elem = popped_node.nxt
            popped_node.next = None
            self.counter -= 1
            return popped_node.value()

    def reversed(self):
        self.nodes.reverse()
        return self.__iter__()


class EmptyListException(Exception):

    def __init__(self, msg):
        self.msg = msg
