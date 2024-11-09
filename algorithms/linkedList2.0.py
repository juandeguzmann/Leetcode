class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class linkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def preappend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def reverseList(self):
        """Reverse the linked list."""
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next  # Store the next node
            current.next = previous   # Reverse the current node's pointer
            previous = current        # Move 'previous' to this node
            current = next_node       # Move to the next node in the list
        self.head = previous          # Update the head to the new front of the list


    def display(self):
        """Print all nodes in the linked list."""
        current = self.head
        while current is not None:
            print(current.data, end = " -> ")
            current = current.next
        print("None") 

ll = linkedList()
ll.append(1)
ll.append(2)
ll.preappend(3)
ll.display()
ll.reverseList()
ll.display()