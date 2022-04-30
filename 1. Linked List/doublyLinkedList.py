class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(Node):
    def __init__(self,head=None):
        self.head = head
        if self.head != None:
            self.length = 1
        else:
            self.length = 0