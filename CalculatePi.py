#  File: CalculatePI.py

#  Description: Homework#3

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 33375

#  Date Created: 2/29/16

#  Date Last Modified: 3/1/16

import math
import random

def computePI(numThrows):
  # initialize sum_darts 
  sum_darts = 0
  counter = 1
  while (counter <= numThrows):
    # generate two random numbers for x and y
    xPos = random.uniform (-1.0, 1.0)
    yPos = random.uniform (-1.0, 1.0)
    # determine if the point is inside the circle
    if (xPos * xPos + yPos * yPos) < 1:
    # if it is add to the sum_darts
      sum_darts += 1 
    # increment counter
    counter += 1
  # compute pi and return the value
  pi = 4.0*sum_darts/counter
  return(pi)

def main():
  # print heading
  print("Computation of PI using Random Numbers")
  print()
  # create a loop that goes from 100 to 10000000
  num = 100
  while (num <= 10000000):
    # call the function to compute pi for num
    print ("num =", '%-8s' % num, end = '   ')
    # compute difference between computed value of pi and math.pi
    dif = computePI(num) - math.pi
    # print the result according to specified format
    print ("Calculated PI = %0.6f" % computePI(num), end = '    ')
    print ("Difference = %+0.6f" % dif)
    # increment num
    num = num * 10
  # print footnote
  print()
  print("Difference = Calculated PI - math.pi")
  
main()

