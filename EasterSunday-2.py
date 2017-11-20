#  File: EasterSunday.py

#  Description: Homework#1

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 33375

#  Date Created: 1/30/16

#  Date Last Modified:2/1/16

def main():
#prompt user to enter year
  year = eval(input("Enter year: "))
  
  a = year%19
  b = year//100
  c = year%100
  d = b//4
  e = b%4
  g = (8*b+13)//25
  h = (19*a+b-d-g+15)%30
  j = c//4
  k = c%4
  m = (a+11*h)//319
  r = (2*e+2*j-k-h+m+32)%7
  n = (h-m+r+90)//25
  p = (h-m+r+n+19)%32

  #print Blank Line
  print()

  #determine which month for the year 
  if (n==3):
    print ("In",year,"Easter Sunday is on",p,"March.")
  elif(n==4):
    print ("In",year,"Easter Sunday is on",p,"April.")

main()
