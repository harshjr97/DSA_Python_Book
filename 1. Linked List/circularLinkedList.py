class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedlist:
    def __init__(self, head=None):
        self.head = head
        self.length = 0
        if self.head != None:
            self.length = 1
        else:
            self.length = 0

    def insertAtBeginning(self, data):
        # create a new node
        newNode = Node(data)
        # if list is empty
        if self.length == 0:
            # make new node as head
            self.head = newNode
            # make head's next as head
            self.head.next = self.head
            # make head's prev as head
            self.head.prev = self.head
        else:
            # make new node's next as head
            newNode.next = self.head
            # make new node's prev as head's prev
            newNode.prev = self.head.prev
            # make head's prev's next as new node
            self.head.prev.next = newNode
            # make head's prev as new node
            self.head.prev = newNode
        # increment length
        self.length += 1

    def insertAtEnd(self, data):
        # create a new node
        newNode = Node(data)
        if self.length == 0:
            # make new node as head
            self.head = newNode
            # make head's next as head
            self.head.next = self.head
            # make head's prev as head
            self.head.prev = self.head
        else:
            # make new node's next as head
            newNode.next = self.head
            # make new node's prev as head's prev
            newNode.prev = self.head.prev
            # make head's prev's next as new node
            self.head.prev.next = newNode
            # make head's prev as new node
            self.head.prev = newNode
        # increment length
        self.length += 1

    def insertAtPosition(self, data, position):
        # if position is less than 0 or greater than length
        if position < 0 or position > self.length:
            print("Position is not valid")
            return
        # if position is 0 then insert at beginning
        if position == 0:
            self.insertAtBeginning(data)
            return
        # if position is length then insert at end
        if position == self.length:
            self.insertAtEnd(data)
            return
        # create a new node
        newNode = Node(data)
        # create a temp node
        temp = self.head
        # traverse to position
        for i in range(position):
            temp = temp.next
        # make new node's next as temp's next
        newNode.next = temp
        # make new node's prev as temp's prev
        newNode.prev = temp.prev
        # make temp's prev's next as new node
        temp.prev.next = newNode
        # make temp's prev as new node
        temp.prev = newNode
        # increment length
        self.length += 1

    def deleteAtBeginning(self):
        # if length is 0 then list is empty
        if self.length == 0:
            print("List is empty")
            return
        # if length is 1
        if self.length == 1:
            # make head as None
            self.head = None
            # make length as 0
            self.length = 0
            return
        # make head as head's next
        self.head = self.head.next
        # make head prev as head prev's prev's
        self.head.prev = self.head.prev.prev
        # make head's prev's next as head
        self.head.prev.next = self.head
        # decrement length
        self.length -= 1

    def deleteAtEnd(self):
        # create a temp node
        temp = self.head
        # create a current node
        current = self.head
        # if length is 0 then list is empty
        if self.length == 0:
            print("List is empty")
            return
        # traverse current to last node till current's next is not head
        while current.next != self.head:
            # make temp as current
            temp = current
            # make current as current's next
            current = current.next
        # make temp's next as head
        temp.next = current.next
        return


    def deleteAtPosition(self, position):
        if position < 0 or position > self.length:
            print("Position is not valid")
            return
        if position == 0:
            self.deleteAtBeginning()
            return
        if position == self.length:
            self.deleteAtEnd()
            return
        # create a temp node
        temp = self.head
        # traverse to position
        for i in range(position):
            temp = temp.next
        # make temp's prev's next as temp's next
        temp.prev.next = temp.next
        # make temp's next's prev as temp's prev
        temp.next.prev = temp.prev
        # decrement length
        self.length -= 1

    def printList(self):
        temp = self.head
        while temp.next != self.head:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)



if __name__ == '__main__':
    c = CircularLinkedlist()
    print("\nInserting at beginning : 1, 2, 3, 4")
    c.insertAtBeginning(1)
    c.printList()
    c.insertAtBeginning(2)
    c.printList()
    c.insertAtBeginning(3)
    c.printList()
    c.insertAtBeginning(4)
    c.printList()
    print("\nInserting at position 2 : 5")
    c.insertAtPosition(5, 2)
    c.printList()
    print("\nInserting at end : 6")
    c.insertAtEnd(6)
    c.printList()
    print("\nInserting at end : 7")
    c.insertAtEnd(7)
    c.printList()
    print("\nDeleting at beginning")
    c.deleteAtBeginning()
    c.printList()
    print("\ndeleting at End")
    c.deleteAtEnd()
    c.printList()
    print("\ndeleting at End")
    c.deleteAtEnd()
    c.printList()
    print("\nDeleting at position 2")
    c.deleteAtPosition(2)
    c.printList()