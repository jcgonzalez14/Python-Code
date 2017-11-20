#  File: FibonacciBase.py

#  Description: Homework#8

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/30/16

#  Date Last Modified: 4/30/16

def main():
  number = eval(input("Enter a number: "))
  a = 0
  b = 1
  c = 0
  d = 0
  fib_list = []
  while d < number:
    d += c
    c = a + b
    a = b
    b = c
    fib_list.append(c)
  rev_list = fib_list[::-1]
  diff = number - rev_list[0]
  print(number, "= ", end = "")
  if rev_list[0] == number:
    print("1", end = "")
    rev_list.pop(0)
  else:
    rev_list.pop(0)
    print("1", end = "")
  for i in rev_list:
    if diff >= i:
      print("1", end = "" )
      diff = diff - i
    else:
      print("0", end = "")
  print(" (fib)")
      

main()
