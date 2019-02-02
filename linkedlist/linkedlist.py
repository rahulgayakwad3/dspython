class ListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        :return: True/False if a list is empty or not
        """
        return self.head is None

    def traverse(self):
        """
        print all elements of a linked list
        """
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

    def insert_front(self, data):
        """
        inserts data in front of linked list
        :param data: data to be inserted
        """
        node = ListNode(data)
        if self.head:
            node.next = self.head
        self.head = node

    def insert_end(self, data):
        """
        inserts data in the end of linked list
        :param data: data to be inserted
        :return:
        """
        node = ListNode(data)
        if self.head:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = node
        else:
            self.head = node

    def find_node(self, data):
        """
        finds the node with given data
        :param data: data to be found
        :return:
        """
        p = self.head
        while p is not None:
            if p.data == data:
                return p
            p = p.next
        return None

    def insert_after_node(self, key, data):
        """
        inserts data after a specific node
        :param key: data of the node after which we want to insert a new node
        :param data: data to be inserted
        :return:
        """
        node = ListNode(data)
        p = self.head
        while p is not None:
            if p.data == key:
                node.next = p.next
                p.next = node
            p = p.next

    def insert_before(self, key, data):
        """
        insert before a specific key
        :param key: key before which insertion has to be made
        :param data: data to be inserted
        :return:
        """
        node = ListNode(data)
        p = self.head
        while p.next is not None:
            if p.next.data == key:
                node.next = p.next
                p.next = node
            p = p.next

    def remove_node(self, data):
        """
        remove a specific node
        :param data:
        :return:
        """
        p = self.head
        while p.next is not None:
            if p.next.data == data:
                temp = p.next
                p.next = p.next.next
                del temp