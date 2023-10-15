class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("none")
    
    def append(self,data):
        new_node= node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    
    def delete(self,data):
        if not self.head:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return 
            current=current.next
            
new_linked=linked_list()
new_linked.display()
new_linked.append(4)
new_linked.append(3)
new_linked.append(6)
new_linked.append(2)
new_linked.display()
new_linked.delete(6)
new_linked.display()   