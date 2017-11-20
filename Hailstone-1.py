#  File: Hailstone.py

#  Description: Homework#3

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 33375

#  Date Created: 2/6/16

#  Date Last Modified:2/10/16

def main():
  # prompt the user to enter the starting number
  start = eval (input ("Enter starting number of the range: "))

  # prompt the user to enter the ending number
  finish = eval (input ("Enter ending number of the range: "))

  # initialize the variables to hold number and max cycle length
  max_num = 0
  max_cycle_length = 0

  # determine the number having the largest cycle length in this range
  # write a loop that goes through all the numbers in that range
  counter = start
  while (counter <= finish):
    # determine the cycle length of each number
    cycle_length = 0
    num = counter
  
    while (num > 1):
      # write the Collatz condition
      if num % 2 == 0:
          num = num / 2
      else:
          num = num * 3 + 1
      
      # increment cycle_length
      cycle_length = cycle_length + 1

    # compare the cycle length of a number with the max cyclelength and
    # replace max cyclelength if cycle length of number is greater or equal
    if (cycle_length >= max_cycle_length):
        max_cycle_length = cycle_length
        max_num = counter
        
        
    counter = counter + 1

 
  # print the result
  print ("The number " + str(max_num) + " has the longest cycle length of " + \
  str(max_cycle_length) + ".")

main()
