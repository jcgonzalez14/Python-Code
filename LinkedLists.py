#  File: LinkedLists.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 10/20/16
#  Date Last Modified: 10/21/16

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = newdata

    def set_next(self, new_next):
        self.next = new_next
    

class LinkedList:

    def __init__(self):
        self.head = None
        self.sizey = 0

    def __str__ (self):
        current = self.head
        julio = ''
        count = 0
        while current != None:
            julio += current.get_data() + "  "
            if count == 9 or count ==19 or count == 29:
                julio += "\n"
            count +=1
            current = current.get_next()
        return(julio)

    def addFirst(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def addLast(self, item):
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.get_next()

        temp = Node(item)

        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            previous.set_next(temp)
            temp.set_next(current)
            
        

    def addInOrder(self,item):       

        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)


    def getLength(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def findUnordered (self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def findOrdered (self, item):

        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def delete (self,item): 
        current = self.head
        chi = self.findUnordered(item)
        previous = None
        found = False
            

        while not found and chi:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def copyList(self):
        current = self.head
        crabby = LinkedList()
        while current != None:
            julio = current.get_data()
            crabby.addLast(julio)
            current = current.get_next()

        return crabby

    def reverseList(self):
        current = self.head
        shitty = LinkedList()
        while current != None:
            joto = current.get_data()
            shitty.addFirst(joto)
            current = current.get_next()

        return shitty

    def orderList (self):
        current = self.head
        horns = LinkedList()
        while current != None:
            puto = current.get_data()
            horns.addInOrder(puto)
            current = current.get_next()

        return horns

    def isOrdered (self):
        current = self.head
        crabby = []
        while current != None:
            julio = current.get_data()
            crabby.append(julio)
            current = current.get_next()

        current = self.head
        batman = []
        while current != None:
            julio = current.get_data()
            batman.append(julio)
            current = current.get_next()

        batman.sort()
        if batman == crabby:
            return True
        else:
            return False

    def isEmpty (self):
        return self.head == None

    def mergeList (self, b):
        current = self.head
        joker = b.head
        ice = LinkedList()
        while current != None:
            if current.get_data() != joker.get_data():
                item = current.get_data()
                itemm = joker.get_data()
                ice.addLast(item)
                ice.addLast(itemm)
                current = current.get_next()
                joker = joker.get_next()
            else:
                current = current.get_next()
                joker = joker.get_next()

        return ice

    def isEqual (self, b):
        current = self.head
        joker = b.head
        equal = True
        meco = self.getLength()
        beco = b.getLength()
        if meco != beco:
            equal = False
        while current != None and equal:
            if current.get_data() == joker.get_data():
                current = current.get_next()
                joker = joker.get_next()
            else:
                equal = False

        return equal

    def removeDuplicates (self):
        current = self.head
        batdog = []
        batcat = LinkedList()
        while current != None:
            item = current.get_data()
            if item not in batdog:
                batcat.addLast(item)
            batdog.append(item)
            current = current.get_next()
        return batcat
            
        
        
            
        
        

            

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
      print ("      node25 not found")
   else:
      print ("      node25 found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 not found")
   else:
      print ("      node34 found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 not found")
   else:
      print ("      node0 found")
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
