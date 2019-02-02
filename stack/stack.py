class Stack(object):
    """
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit=10):
        self.stack = list()
        self.limit = limit

    def is_empty(self):
        return self.stack == []

    def push(self,data):
        if len(self.stack) >= self.limit:
            raise MemoryError
        self.append(data)

    def pop(self):
        if self.is_empty():
            print("Cannot pop from an Empty Stack")
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)