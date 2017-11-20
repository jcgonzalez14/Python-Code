#  File: htmlChecker.py
#  Description:
#  Student's Name: Julio Gonzalez
#  Student's UT EID: jcg3245
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 10/4/16
#  Date Last Modified:

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



def getTag(file):

    filey = file.read()
    tag = ''
    for i in range(len(filey)):
        if filey[i] == "<":
            i +=1
            while filey[i] != ">" and filey[i] != " ":
                tag += filey[i]
                i +=1
            tag = tag + ' '
        else:
            i +=1
    return tag


def main():
   f = open ("htmlfile.txt", "r")
   tag = getTag(f)
   List_of_tags = tag.split()
   print(List_of_tags)
   print()
   
   VALIDTAGS = []
   EXCEPTIONS = ["meta", "br", "hr"]

   stacky = Stack()

   for tag in List_of_tags:
      if tag[0] != "/" and tag in EXCEPTIONS:
         print("Tag is: ",tag,":does not need to match: stack is still: ",stacky)
      elif tag[0] != "/":
         if tag not in VALIDTAGS:
            print("Tag",tag,"not recognized, but its cool")
            VALIDTAGS.append(tag)
         stacky.push(tag)
         print("Tag is: ",tag,"pushed: stack is now", stacky)
      elif tag[1:] == stacky.peek():
         stacky.pop()
         print("Tag is,",tag,"matches: stack is now", stacky)
      else:
         print("You fucked up. This tag",tag,"doesn't match",stacky.peek())
         break
   print()

   if stacky.isEmpty():
      print ("Processing Complete. No mismatches found")

   else:
      print("Processing complete. Unmatches tags on stack", stacky)

   print("all tags found and accepted:", VALIDTAGS)
   print("exeptions found:", EXCEPTIONS)
   
      

      
         
         
            
        

        


main()
