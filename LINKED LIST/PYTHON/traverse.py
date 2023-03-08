class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #initially the next part of the node is empty

class LinkList():
    def __init__(self):
        self.head=None
    
    def display(self):
        if(self.head is None):
            print("Empty List")
        
        else:
            traverse=self.head
            while(traverse is not None):
                print(traverse.data)
                traverse=traverse.next
    

    
                
        