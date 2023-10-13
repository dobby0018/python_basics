#first we need to create 2 classes 
# 1)node class
# 2)linked list class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print("self.head",self.head)
            return
        current = self.head
        while current.next:
            current = current.next
            print("current next",current.next)
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Create a new linked list
my_linked_list = LinkedList()

# Add elements to the list
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

# Display the linked list
# my_linked_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> None

# # Insert an element at the beginning
# my_linked_list.prepend(0)

# # Display the linked list
# my_linked_list.display()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> None

# # Delete an element
# my_linked_list.delete(2)

# # Display the linked list
# my_linked_list.display()  # Output: 0 -> 1 -> 3 -> 4 -> None


        