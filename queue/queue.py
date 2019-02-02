class Queue(object):

    def __init__(self):
        self.q = list()

    def is_empty(self):
        return self.q == []

    def size(self):
        return len(self.q)

    def add_to_queue(self, data):
        if self.is_empty():
            self.q.append(data)
        elif self.size() == 1:
            temp = self.q[0]
            self.q[0] = data
            self.q.append(temp)
        else:
            for k in range(len(self.q)-1):
                self.q[k+1] = self.q[k]
            self.q[0] = data

    def remove_from_queue(self):
        if self.is_empty():
            print("Cannot dequeue an empty queue")
        else:
            return self.q.pop()


class Deque(Queue):

    def add_to_queue_right(self, data):
        self.q.append(data)

    def remove_from_left(self):
        if self.is_empty():
            print("Cannot remove from an empty deque")
        else:
            temp = self.q[0]
            for k in range(len(self.q)-1):
                self.q[k] = self.q[k+1]
            return temp