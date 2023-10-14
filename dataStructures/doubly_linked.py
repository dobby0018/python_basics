class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def insert_after(self, prev_data, new_data):
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == prev_data:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
        print(f"{prev_data} not found in the list. Insertion failed.")

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next
        print(f"{data} not found in the list. Deletion failed.")

# Create a doubly linked list
my_doubly_linked_list = DoublyLinkedList()

# Append elements
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

# Display the list forward and backward
print("Doubly Linked List (Forward):")
my_doubly_linked_list.display_forward()
print("Doubly Linked List (Backward):")
my_doubly_linked_list.display_backward()

# Insert an element after 2
my_doubly_linked_list.insert_after(2, 4)

# Display the list after insertion
print("Doubly Linked List after insertion (Forward):")
my_doubly_linked_list.display_forward()
print("Doubly Linked List after insertion (Backward):")
my_doubly_linked_list.display_backward()

# Delete an element from the list
my_doubly_linked_list.delete(1)

# Display the list after deletion
print("Doubly Linked List after deletion (Forward):")
my_doubly_linked_list.display_forward()
print("Doubly Linked List after deletion (Backward):")
my_doubly_linked_list.display_backward()
