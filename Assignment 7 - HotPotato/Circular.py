class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def __str__ (self):
        return self.data
    
class CircularList(object):

    def __init__ (self): 
      # the circular list constructor method.
        self.head = None
    
    def add (self,item):
      # Insert an element in the list.  You will need this to build your
      # circular list from the data strings in the input file.  Hint:  figure
      # out which of the "add" methods we've discussed in class to use is
      # useful here and use it as a template for this method.
        ptr = Node(item)
        temp = self.head
         
        ptr.next = self.head
 
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr
        else:
            ptr.next = ptr
 
        self.head = ptr

    def addLast (self, item): 
        if self.head is None:
            self.add(item)
            return
        current = self.head
        while (current.next != self.head):
            current = current.next
        temp = Node(item)
        current.next = temp
        temp.next = self.head
        
    def isEmpty (self):
      # Return True if the cicrcular list is empty.
      return self.head == None
    
    def onlyOneNode (self):
      # Return True if there is only one node left in the circular list.
      # This would be the "survivor".
        return self.head.next == self.head
    
    def remove (self,current,previous):
      # Delete the node pointed to by "current" from the circular list.
      # Pass the "previous" pointer along for convenience.  This method
      # would only be called if there are at least 2 nodes in the list.
      # Return a pointer to the node immediately following the deleted
      # one.  Hint:  be sure to correctly handle the case where you delete
      # the first node in the circular list.
        if current == self.head:
            previous.next = self.head.next
            self.head = self.head.next
            return
        temp = self.head
        while (temp != current):
            temp = temp.next
        previous.next = current.next
    
    def __str__ (self):
      # Return a string representation of the circular list.  It should
      # include line breaks after every ten elements in the list.
        players = []
        counter = 0;
        temp = self.head
        if self.head is not None:
            while(True):
                if counter == 10:
                    players.append('\n')
                    counter = 0
                players.append(temp.data)
                t = temp.data
                counter += 1
                temp = temp.next
                if (temp == self.head):
                    break
        return ' '.join(players)
    
    def play(self, n):
       iteration = 1
       current = self.head
       while (not self.onlyOneNode()):
          for i in range(0, n-1):
              previous = current
              current = current.next
          print('Iteration # ' + str(iteration))
          print('Removing player ' + current.data)
          self.remove(current, previous)
          print(self, end='\n\n')
          current = current.next
          iteration += 1
       print('The sole survivor is: ' + current.data)
       print('----')
       
def main():
    in_file = open ("HotPotatoData.txt", "r")
    line = in_file.readline()
    while line:
       line = line.strip()
       items = line.split()
       if len(items) == 2:
          game = CircularList()
          numNames = int(items[0])
          n = int(items[1])
       for i in range(0, numNames):
          line = in_file.readline()
          line = line.strip()
          game.addLast(line)
       game.play(n)
       line = in_file.readline()
    in_file.close()

              
main()
