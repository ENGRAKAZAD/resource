class Node:
 def __init__(self,data,next=None):
     self.data = data
     self.next = next
     
class linkedList:
    def __init__(self):
        self.head = None
        
    def printall(self):
        tmp = self.head
        while(tmp != None):
            print(tmp.data)
            tmp=tmp.next
            
    def push(self,data):
      nowNode = Node(data)
      if(self.head == None):
          self.head = nowNode
      else:
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = nowNode
    def lenth(self):
      current=self.head
      total=0
      while(current.next!=None):
         current=current.next
         total+=1
      return total
      
      

objlist=linkedList()
objlist.push(10)
objlist.push(40)
objlist.push(170)
objlist.push(1000)

objlist.printall()
print("Length is :",objlist.lenth())
    
