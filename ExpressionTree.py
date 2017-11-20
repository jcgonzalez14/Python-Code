#  File: ExpressionTree.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 11/15/16
#  Date Last Modified: 11/15/16

45/100

class Stack (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items [len(self.items)-1]

   def size (self):
      return len(self.items)

   def __str__ (self):
      return str(self.items)


class BinaryTree:

    def __init__(self,initVal):
        self.data = initVal
        self.left = None
        self.right = None

##    def createTree (self,expr):
##
##    def evaluate (self, root):
##
##    def preOrder (self, root):
##
##    def postOrder (self, root):
        



    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self,value):
        self.data = value

    def getRootVal(self):
        return self.data

def main():

    file = open("treedata.txt", "r")
    for i in file:
        print("Infix expression: ",i)


main()
