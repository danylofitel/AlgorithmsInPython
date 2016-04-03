__author__ = 'Danylo'


# Singly linked list node
class SllNode:
    def __init__(self, value):
        self.value = value
        self.nxt = None


# Doubly linked list node
class DllNode:
    def __init__(self, value):
        self.value = value
        self.prv = None
        self.nxt = None
