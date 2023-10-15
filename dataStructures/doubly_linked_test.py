class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Doubly:
    def __init__(self):
        self.head=None
    
    def display_front(self):
        if not self.head:
            print("the list is empty!!!")
            return
        else:
            current=self.head
            while current:
                print(current.data,end="<->")
                current=current.next
            print("none")
            
    def display_back(self):
        if not self.head:
            print("list empty")
            return
        else:
            current=self.head
            while current.next:
                current=current.next
            while current:
                print(current.data,end="<->")
                current=current.prev
            print("none")
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        else:
            current=self.head
            while current.next:
                current=current.next
            new_node.prev=current
            current.next=new_node
            return

new_list=Doubly()
new_list.append(7)
new_list.append(5)
new_list.display_back()