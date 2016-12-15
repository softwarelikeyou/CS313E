# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

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
         return ''
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
   
   def addInOrder (self, item): 
      if self.isEmpty():
         self.addFirst(item)
         return
       
      current = self.head.getNext()
      previous = self.head
    
      stop = False
        
      while current != None and not stop:
         if current.getData() > item:
            stop = True
         else:
            previous = current
            current = current.getNext()
            
      temp = Node(item)
      temp.setNext(current)
      if previous == self.head:
         temp.setNext(self.head)
         self.head = temp
      else:
         previous.setNext(temp)
   
   def getLength (self):
      count = 0
      current = self.head
      if current == None:
         return count
      else:
         count = 1
      while (current.getNext() != None):
         count += 1
         current = current.getNext()
      return count
   
   def findUnordered (self, item): 
      found = False
      current = self.head
      if current == None:
         return found
      while (current.getNext() != None):
         if current.getData() == item:
            found = True
            break
         current = current.getNext()
      return found
   
   def findOrdered (self, item):
      current = self.head
      found = False
      stop = False
      while current != None and not found and not stop:
         if current.getData() == item:
            found = True
         else:
            if current.getData() > item:
               stop = True
            else:
               current = current.getNext()

      return found

   def delete (self, item):
      current = self.head
      previous = None
      found = False

      while not found and current != None:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if found:
          if previous == None:
             self.head = current.getNext()
          else:
             previous.setNext(current.getNext())
         
      return found

   def copyList (self):
      tempLinkList = LinkedList()
      current = self.head
      while current != None:
         currentData = current.getData()
         tempLinkList.addLast(currentData)
         current = current.getNext()
      return tempLinkList
   
   def reverseList (self): 
      reversed = LinkedList()
      current = self.head
      while current != None:
         reversed.addFirst(current.getData())
         current = current.getNext()
      return reversed
   
   def orderList (self): 
      results = LinkedList()
      data = []
      current = self.head
      while current != None:
         data.append(current.getData())
         current = current.getNext()

      self.quickSort(data)

      for value in data:
         results.addLast(value)
         
      return results

   def quickSort(self, alist):
      self.quickSortHelper(alist,0,len(alist)-1)

   def quickSortHelper(self, alist, first, last):
      if first<last:
         splitpoint = self.partition(alist, first, last)
         self.quickSortHelper(alist, first, splitpoint-1)
         self.quickSortHelper(alist, splitpoint+1, last)

   def partition(self, alist, first, last):
      pivotvalue = alist[first]
      leftmark = first+1
      rightmark = last

      done = False
      while not done:
         while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

         while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

         if rightmark < leftmark:
            done = True
         else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

      temp = alist[first]
      alist[first] = alist[rightmark]
      alist[rightmark] = temp

      return rightmark

   def isOrdered (self):
      order = True
      current = self.head
      # TODO: what to return if list is empty?
      while current.getNext() != None:
         if current.getData() > current.getNext().getData():
            order = False
            break
         current = current.getNext()
         
      return order
   
   def isEmpty (self): 
      return self.head == None
   
   def mergeList (self, b):
      current = b.head
      while current != None:
          self.addInOrder(current.getData())
          current = current.getNext()
      return self.orderList()
      
   def isEqual (self, b):
      if self.getLength() != b.getLength():
          return False
      result = True
      currentSelf = self.head
      currentB = b.head
      while currentSelf != None and currentB != None:
         if currentSelf.getData() != currentB.getData():
            result = False
            break
         currentSelf = currentSelf.getNext()
         currentB = currentB.getNext()
      return result
    
   def removeDuplicates (self):
      words_dict = {}
      current = self.head
      if current == None:
         return self
         
      count = 0
      while current != None:
         if current.getData() in words_dict:
            words_dict[current.getData()] = words_dict[current.getData()] + 1
         else:
            words_dict[current.getData()] = 1
         current = current.getNext()

      copy = self.copyList()
      
      for key, value in words_dict.items():
         for i in range (value, 1, -1):
            copy.delete(key)
          
      return copy
    
def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

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

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
