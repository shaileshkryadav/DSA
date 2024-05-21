class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1 
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next 

newLinkedList = Linkedlist(3)
newLinkedList.append(4)
newLinkedList.append(5)
newLinkedList.printList()
