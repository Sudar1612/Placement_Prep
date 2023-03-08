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
    
    #add elements at begining
    def addAtBegin(self,data):
        #check if list is empty
        if(self.head is None):
            newNode=Node(data)
            self.head=newNode
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
    
    #add elements at end
    def addAtEnd(self,data):
        if(self.head is None): #check for empty list
            self.addAtBegin(data)
        else:
            newNode=Node(data)
            lastNode=self.head
            while(lastNode.next is not None):   #loop to find the lastnode
                lastNode=lastNode.next

            lastNode.next=newNode
    
    def insertAfter(self,data,after):
        if(self.head is None): #check for empty list
            self.addAtBegin(data)
        else:
            newNode=Node(data)
            traverse=self.head
            while(traverse is not None):
                if(traverse.data==after):
                    newNode.next=traverse.next
                    traverse.next=newNode
                    return None
                traverse=traverse.next
            if(traverse is None):
                print("Node not in Linked List")
    
    def insertBefore(self,data,before):
        if(self.head is None or self.head.data==before ): #check for empty list
            self.addAtBegin(data)
            return None
        newNode=Node(data)
        traverse=self.head
        while(traverse is not None):
            if(traverse.next.data==before):
                newNode.next=traverse.next
                traverse.next=newNode
                return None
            traverse=traverse.next
        if(traverse is None):
            print("Element not in List")
    
    def del_start(self):
        if(self.head is None):
            print("Empty List")
            return None
        self.head=self.head.next
    
    def del_end(self):
        if(self.head is None):
            print("Empty List")
        elif(self.head.next is None):
            self.head=None
        else:
            traverse=self.head
            while(traverse.next.next is not None):
                traverse=traverse.next
            traverse.next=None
            

        


 
link=LinkList()
print("Insertion")
link.addAtBegin(10)
link.addAtEnd(20)
link.insertAfter(15,10)
link.insertBefore(16,20)
link.insertBefore(5,10)
link.display()
print("Deletion")
link.del_start()
link.del_end()
link.display()
