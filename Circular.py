#  File: Circular.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 10/24/16
#  Date Last Modified: 10/26/16

    
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.last = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def get_last(self):
        return self.last
    
    def set_data(self, new_data):
        self.data = newdata

    def set_next(self, new_next):
        self.next = new_next

    def set_last(self, new_last):
        self.last = new_last

class CircularList(object):

    def __init__ (self): 
        self.head = None
        self.sizey = 0

    def add (self,item):
        self.sizey +=1
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

    def delete (self,item): 
        current = self.head
        previous = None
        prepre = None
        rcount = 0
        while self.sizey != 1:
            for i in range(item):
                prepre = previous
                previous = current
                current = current.get_next()
            self.sizey -= 1
            rcount +=1
            print("dude killed is in round",rcount,"is:")
            print(previous.get_data())
            prepre.set_next(previous.get_next())
        return (prepre.get_data())


    def isEmpty (self):
        return self.head == None
            
    def make_circle(self):
        current = self.head
        last = self.head
        while current != None:
            previous = current
            current = current.get_next()
        previous.set_last("yes")
        previous.set_next(last)
    

    def __str__ (self):
        current = self.head
        julio = ''
        for i in range(self.sizey):
            julio = julio+"  "+current.get_data()
            current = current.get_next()
        julio = julio+"  "+current.get_data()
        return(julio)


def main():

    in_file = open ("HotPotatoData.txt", "r")

    
    for line in in_file:
        if line[0].isalpha () == False:
            line = line.strip()
            line = line.split()
            numPeople = int(line[0])
            hit = int(line[1])
            mylist = CircularList()
        for i in range(numPeople):
            st1 = in_file.readline()
            mylist.add(st1)
        mylist.make_circle()
        justin = mylist.delete(hit)
        print("The sole survivor is:",justin)
        


main()
