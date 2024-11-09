class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None: #if self.head is empty to the following
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None: #while the current.next is not empty, keep looping
            current = current.next #Update current to the next node
        current.next = new_node #Once current.next is None, break out of the loop and set current.next as the new node.

    def display(self):
        """Print all nodes in the linked list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list

ll = linkedList()
ll.append(1)
ll.append(2)
ll.display()
