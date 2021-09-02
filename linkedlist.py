class Node:
 def __init__(self,data,next=None):
     self.data=data
     self.next=next
     
class linkedList:
    def __init__(self):
        self.head=None
        
    def printall(self):
        tmp=self.head
        while(tmp!=None):
            print(tmp.data)
            tmp=tmp.next
            
            
first=Node(10)
second=Node(20)
third=Node(30)


objList=linkedList()

objList.head=first
first.next=second
second.next=third

objList.printall()
    