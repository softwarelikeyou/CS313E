class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedList:   
    def __init__(self):
        self.head = None
      
    def __str__ (self):
        if self.head == None:
            return
        current = self.head
        count = 0
        string = ''
        while current != None:
            string += current.getData() + '  '
            count += 1
            current = current.getNext()
        if count%10 == 0:
            string += "\n"
        return string
      
    def addFirst (self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def addLast (self, item): 
        if self.isEmpty():
            self.addFirst(item)
            return
        current = self.head
        while (current.getNext() != None):
            current = current.getNext()
        temp = Node(item)
        current.setNext(temp)
    #def addInOrder(self, item):

    def isEmpty (self): 
      # Return True if a list is empty, or False otherwise
        return self.head == None

def main():
   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)
main()
    
