class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def read(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            raise BufferEmptyException("The buffer is empty")

    def write(self, data):
        if len(self.storage) == self.capacity:
            raise BufferFullException("The buffer is full")
        else:
            self.storage.append(data)

    def overwrite(self, data):

        if len(self.storage) == self.capacity:
            self.storage.pop(0)
            self.storage.append(data)
        elif len(self.storage) > 0:
            self.storage.append(data)
        else:
            raise BufferEmptyException("The buffer is empty")

    def clear(self):
        if len(self.storage) > 0:
            self.storage.clear()
