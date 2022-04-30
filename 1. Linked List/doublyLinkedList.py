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


    def insertAtBegining(self,data):
        # create new node and assign data to it
        newNode = Node(data)
        # if list is empty, make newNode as head
        if self.length==0:
            self.head = newNode
        else:
            # make next of new node as head
            newNode.next = self.head
            # make prev of head as newNode
            self.head.prev = newNode
            # make newNode as head
            self.head = newNode
        # increment length
        self.length += 1

    def insertAtEnd(self,data):
        # create new node and assign data to it
        newNode = Node(data)
        # if list is empty, make newNode as head
        if self.length == 0:
            self.head = newNode
        else:
            # traverse to the last node and assign next of it as newNode
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            # make prev of newNode as temp
            newNode.prev = temp
        # increment length
        self.length += 1

    def insertAtPosition(self,data,position):
        # if position is 0, insert at beginning
        if position == 0:
            self.insertAtBegining(data)
        # if position is equal to length, insert at end
        elif position == self.length:
            self.insertAtEnd(data)
        # if position is in between, insert at position and increment length
        else:
        # create new node and assign data to it
            newNode = Node(data)
            # traverse to the position
            temp = self.head
            while position > 1:
                temp = temp.next
                position -= 1
            # make next of newNode as temp
            newNode.next = temp.next
            # make prev of temp as newNode
            newNode.prev = temp
            # make next of temp as newNode
            temp.next.prev = newNode
            # make temp as newNode
            temp.next = newNode
        # increment length
        self.length += 1

    def deleteFromBeginning(self):
        # if list is empty, return
        if self.length == 0:
            return
        # if list has only one node, make head as None
        elif self.length == 1:
            self.head = None
        # if list has more than one node, make next of head as head
        else:
            self.head = self.head.next
        # decrement length
        self.length -= 1

    def deleteFromEnd(self):
        # if list is empty, return
        if self.length == 0:
            return
        # if list has only one node, make head as None
        elif self.length == 1:
            self.head = None
        # if list has more than one node, traverse to the last node and make next of it as None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
        # decrement length
        self.length -= 1

    def deleteFromPosition(self,position):
        # if list is empty, return
        if self.length == 0:
            return
        # if position is 0, delete from beginning
        elif position == 0:
            self.deleteFromBeginning()
        # if position is equal to length, delete from end
        elif position == self.length:
            self.deleteFromEnd()
        # if position is in between, delete from position and decrement length
        else:
            temp = self.head
            while position > 1:
                temp = temp.next
                position -= 1
            temp.next = temp.next.next
            self.length -= 1

    def printList(self):
        temp = self.head
        while temp != None:
            if temp.next != None:
                print(temp.data,end=" <-> ")
            else:
                print(temp.data)
            temp = temp.next
        print()


d = DoublyLinkedList()
d.insertAtBegining(1)
d.insertAtEnd(2)
d.insertAtEnd(3)
d.insertAtEnd(4)
d.insertAtEnd(5)
d.insertAtEnd(6)
d.insertAtEnd(7)
d.insertAtEnd(8)
d.insertAtBegining(0)
d.printList()