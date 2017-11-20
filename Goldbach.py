#  File: Goldbach.py

#  Description: Homework#3

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 33375

#  Date Created: 2/27/16

#  Date Last Modified:2/27/16

def is_prime (n):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor = divisor + 1
  return True

def main():
  # prompt the user to enter the lower limit lo
  lo = eval (input ("Enter starting number of the range: "))
 
  # prompt the user to enter the upper limit hi
  hi = eval (input ("Enter ending number of the range: "))

  #Error checking
  while lo < 4 or lo % 2 !=0 or hi < lo or hi % 2 != 0:
    lo = eval (input ("Enter starting number of the range: "))
    hi = eval (input ("Enter ending number of the range: "))

# Write an outer while loop that goes from lo to hi in steps of 2
  counter = lo
  while (counter <= hi):
    # print counter
    print (counter, end = '', )

    #start finding primes!
    # Write an inner loop with a loop counter num
    # Set num to be equal to 2
    num = 2
    # Set limit to be half of counter
    limit = counter // 2 
    while (num <= limit):
      # test if num and (counter - num) are primes.
      if (is_prime(num) == True):
         if (is_prime(counter - num) == True):
           print (" =", num, "+", (counter - num), end = '')          
      num = num + 1
    print ()
    counter = counter + 2

main()
