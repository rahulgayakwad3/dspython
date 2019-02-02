class ListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def traverse(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

    def insert_front(self, data):
        node = ListNode(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        node = ListNode(data)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node

    def find_node(self, data):
        p = self.head
        while p is not None:
            if p.data == data
                return p
            p = p.next
        return None

    def insert_after(self, key, data):
        node = ListNode(data)
        p = self.head
        while p is not None:
            if p.data == key:
                node.next = p.next
                p.next = node
            p = p.next

    def insert_before(self, key, data):
        node = ListNode(data)
        p = self.head
        while p.next is not None:
            if p.next.data == key:
                node.next = p.next
                p.next = node
            p = p.next

    def remove_node(self, data):
        p = self.head
        while p.next is not None:
            if p.next.data == data:
                p.next = p.next.next