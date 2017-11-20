#  File: ISBN.py

#  Description: Homework#8

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 33375

#  Date Created: 3/30/16

#  Date Last Modified: 3/31/16

def sum_num (a):
  sum_n = 0
  for i in range (len(a)):
    sum_n += a[i]
  return sum_n

def main():
  # open file for reading
  inFile =  open ("./isbn.txt", "r")
  in_dile =  open ("./isbnOut.txt", "w")
  

  for line in inFile:
    #  process the line
    line = line.rstrip("\n")   # strip the newline character at the end
    fine = line
    line = line.replace("-","")
    if len(line) == 10 and (line[0:9].isdigit()) and ((line.endswith("X")) or (line.endswith("x")) or (line[-1].isdigit())):
      first = line[0:9]
      isbn = []
      s1 = []
      s2 = []
      s3 = []
  
      for i in first:
        isbn.append(int(i))
        s1.append(sum_num(isbn))
      if (line.endswith("X") or line.endswith("x")):
        s1.append(sum_num(isbn) + 10)
      else:
        s1.append(sum_num(isbn) + int(line[-1]))
      
  
      for i in s1:
        s3.append(int(i))
        s2.append(sum_num(s3))
      
      if ((s2[-1]) % 11 )== 0:
        print(fine, "valid")
        in_dile.write(fine)
        in_dile.write ("  valid \n")
      else:
        in_dile.write (fine)
        in_dile.write ("  invalid \n")
        print(fine, " invalid")
    
      
    else:
      in_dile.write (fine)
      in_dile.write ("  invalid \n")
      print(fine, "invalid")
  
  inFile.close()
  in_dile.close()
    

main()
  
