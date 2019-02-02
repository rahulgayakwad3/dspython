class StackOverFlowError(BaseException):
    pass


class Stack(object):
    """
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self):
        self.stack = list()

    def is_empty(self):
        """
        returns True/False to checkout if stack is empty
        :return:
        """
        return self.stack == []

    def push(self, data):
        """
        push an element to stack
        :param data: data to be added
        :return:
        """
        try:
            self.append(data) # if space is full raise exception
        except MemoryError:
            raise StackOverFlowError("Insufficient Memory, Free up some space")

    def pop(self):
        """
        returns the top element from the stack
        :return:
        """
        if self.is_empty():
            print("Cannot pop from an Empty Stack")
        else:
            return self.stack.pop()

    def size(self):
        """
        returns size of the currect team
        :return:
        """
        return len(self.stack)

