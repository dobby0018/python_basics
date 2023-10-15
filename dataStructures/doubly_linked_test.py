class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Doubly:
    def __init__(self):
        self.head=None
    
    def display(self):
        if not self.head:
            print("the list is empty!!!")
            return
        else:
            current=self.head
            while current:
                print(current.data,end="->")
                current=current.next