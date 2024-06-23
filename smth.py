class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, data):
        if prev_node is None:
            print("Error!")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

ll = LinkedList()

ll.append(10)
ll.printlist()

ll.append(20)
ll.printlist()

ll.append(30)
ll.printlist()

ll.append(40)
ll.printlist()

ll.append(50)
ll.printlist()
