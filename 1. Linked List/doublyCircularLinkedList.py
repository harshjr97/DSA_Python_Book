class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyCircularLinkedList:
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
        if position < 0 or position > self.length:
            print("Position is out of range")
            return
        if position == 0:
            self.insertAtBeginning(data)
            return
        if position == self.length:
            self.insertAtEnd(data)
            return
        # create a new node
        newNode = Node(data)
        # find the node at position
        temp = self.head
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

    def deleteAtPosition(self, position):
        if position < 0 or position > self.length:
            print("Position is out of range")
            return
        if position == 0:
            self.deleteAtBeginning()
            return
        if position == self.length:
            self.deleteAtEnd()
            return
        # find the node at position
        temp = self.head
        for i in range(position):
            temp = temp.next
        # make temp's prev's next as temp's next
        temp.prev.next = temp.next
        # make temp's next's prev as temp's prev
        temp.next.prev = temp.prev
        # decrement length
        self.length -= 1

    def deleteAtBeginning(self):
        if self.length == 0:
            return
        else:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.head = None
            else:
                self.head.prev = self.head.next
                self.head.next = self.head.prev
    
    def deleteAtEnd(self):
        if self.length == 0:
            return
        else:
            self.head = self.head.prev
            self.length -= 1
            if self.length == 0:
                self.head = None
            else:
                self.head.prev = self.head.next
                self.head.next = self.head.prev

    def printList(self):
        if self.length == 0:
            print("List is empty")
            return
        temp = self.head
        for i in range(self.length):
            if i == self.length - 1:
                print(temp.data)
            else:
                print(temp.data, end="  <->  ")
            temp = temp.next
        print()



if __name__ == "__main__":
    # create a linked list
    linkedList = DoublyCircularLinkedList()
    # insert at beginning
    linkedList.insertAtBeginning(1)
    linkedList.insertAtBeginning(2)
    linkedList.insertAtBeginning(3)
    linkedList.insertAtBeginning(4)
    linkedList.insertAtBeginning(5)
    # insert at end
    linkedList.insertAtEnd(6)
    linkedList.insertAtEnd(7)
    # print list
    linkedList.printList()
    # delete at beginning
    linkedList.deleteAtBeginning()
    linkedList.printList()
    # delete at end
    linkedList.deleteAtEnd()
    linkedList.printList()
