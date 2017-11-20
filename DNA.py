#  File: DNA.py

#  Description: Homework#8

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 33375

#  Date Created: 3/25/16

#  Date Last Modified: 3/26/16

def main():
    inFile = open ("./dna.txt", "r")

    num_pairs = inFile.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int (num_pairs)
    print("Longest common sequnce")
    print()
    nug = 1 
    for i in range (num_pairs):
      print ("Pair",nug, end = ': ')
      st1 = inFile.readline()
      st2 = inFile.readline()


      st1 = st1.strip()
      st2 = st2.strip()

      st1 = st1.upper()
      st2 = st2.upper()

      if (len(st1) > len(st2)):
          dna1 = st1
          dna2 = st2
      else:
          dna1 = st2
          dna2 = st1
      
      # get all substrings of dna2
      wnd = len (dna2)
      flag = True
      nug = nug + 1 
      while (wnd > 0 and flag == True):
        start_idx = 0
        while ((start_idx + wnd) <= len (dna2)):
          sub_strand = dna2[start_idx: start_idx + wnd]
          if (dna1.find(sub_strand) != -1):
              print (sub_strand)
              flag = False
          # move starting place by 1
          start_idx += 1
        # decrease window size
        wnd = wnd - 1
      if flag == True:
        print ("No Common Sequence Found")
main()
