class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("Circular linked list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")

    def insert_after(self, prev_data, new_data):
        new_node = Node(new_data)
        if not self.head:
            print("List is empty. Insertion failed.")
            return
        current = self.head
        while True:
            if current.data == prev_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                break
        print(f"{prev_data} not found in the list. Insertion failed.")

    def delete(self, data):
        if not self.head:
            print("List is empty. Deletion failed.")
            return
        current = self.head
        prev = None
        while True:
            if current.data == data:
                if prev:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                else:
                    temp = current
                    while current.next != self.head:
                        current = current.next
                    current.next = temp.next
                    self.head = temp.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break
        print(f"{data} not found in the list. Deletion failed.")

# Create a circular linked list
my_circular_linked_list = CircularLinkedList()

# Append elements
my_circular_linked_list.append(1)
my_circular_linked_list.append(2)
my_circular_linked_list.append(3)

# Display the list
print("Initial circular linked list:")
my_circular_linked_list.display()

# Insert an element after 2
my_circular_linked_list.insert_after(2, 4)

# Display the list after insertion
print("Circular linked list after insertion:")
my_circular_linked_list.display()

# Delete an element from the list
my_circular_linked_list.delete(1)

# Display the list after deletion
print("Circular linked list after deletion:")
my_circular_linked_list.display()
