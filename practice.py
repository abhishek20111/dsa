class Node:
    def __init__(self, name=None, next = None):
        self.name = name
        self.next = next

class Link_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
