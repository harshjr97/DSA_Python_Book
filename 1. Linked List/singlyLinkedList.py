# node of a singly linked list
class Node:

    def __init__(self,data=None):
        self.data = None
        self.next = None


class LinkedList(Node):

    def __init__(self,head=None):
        self.head = head
        if self.head != None:
            self.length = 1
        else:
            self.length = 0

    
    def insertAtBeginning(self, data):
        # create new node and assign data to it
        newNode = Node()
        newNode.data = data
        # if list is empty, make newNode as head
        if self.length ==0:
            self.head = newNode
        # make next of new node as head if list is not empty
        else:
            newNode.next = self.head
            self.head = newNode
        # increment length
        self.length += 1

    def insertAtEnd(self, data):
        # create new node and assign data to it
        newNode = Node()
        newNode.data = data
        # if list is empty, make newNode as head
        if self.length == 0:
            self.head = newNode
        # traverse to the last node and assign next of it as newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        # increment length
        self.length += 1
    
    def insertAtPosition(self, data, position):
        # if position is 0, insert at beginning
        if position == 0:
            self.insertAtBeginning(data)
        # if position is equal to length, insert at end
        elif position == self.length:
            self.insertAtEnd(data)
        # if position is in between, insert at position and increment length
        else:
        # create new node and assign data to it
            newNode = Node()
            newNode.data = data
            # traverse to the position
            temp = self.head
            for i in range(position-1):
                temp = temp.next
            # make next of new node as next of temp
            newNode.next = temp.next
            # make next of temp as newNode
            temp.next = newNode
            self.length += 1
    
    def deleteFromBeginning(self):
        # if list is empty, return
        if self.length == 0:
            print("List is empty")
        # else make next of head as head and decrement length
        else:
            self.head = self.head.next
            self.length -= 1
    
    def deleteFromEnd(self):
        # if list is empty, return
        if self.length == 0:
            print("List is empty")
        # else traverse to the last second node and make next of it as None and decrement length
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
            self.length -= 1
    
    def deleteFromPosition(self, position):
        # if position is 0, delete from beginning
        if position == 0:
            self.deleteFromBeginning()
        # if position is equal to length, delete from end
        elif position == self.length:
            self.deleteFromEnd()
        # if position is in between, delete from position and decrement length
        else:
            # traverse to the position
            temp = self.head
            for i in range(position-1):
                temp = temp.next
            # make next of temp as next of next of temp
            temp.next = temp.next.next
            self.length -= 1

    def printList(self):
        temp = self.head
        while temp != None:
            if temp.next == None:
                print(temp.data)
            else:
                print(temp.data, end = " -> ")
            temp = temp.next
        print()
        
l = LinkedList()
l.insertAtBeginning(1)
l.insertAtBeginning(2)
l.insertAtBeginning(3)
l.insertAtEnd(4)
l.insertAtEnd(5)
l.insertAtPosition(6,2)
l.printList()