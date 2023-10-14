class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node= Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("none")
        
new_linked=linked_list()
new_linked.append(3)
new_linked.append(5)
new_linked.append(4)
new_linked.display()
        