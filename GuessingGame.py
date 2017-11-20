#  File: GuessingGame.py

#  Description: Homework#8

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/12/16

#  Date Last Modified: 4/12/16

def main():
  a=[]
  i=1
  while i <=100:
    a.append(i)
    i+=1
  print('Think of a number between 1 and 100 inclusive.')
  print('And I will guess what it is in 7 tries or less.')
  print()
  ready = input('Are you ready? (y/n): ')
  while (ready != 'y') and (ready != 'n'):
    ready = input('Are you ready? (y/n): ')
  count = 1
  if ready == 'y':
    lo = 1
    hi = len(a)
    while (lo <= hi):
      mid = round((lo + hi) // 2)
      print("Guess ", count,":  The number you thought was", mid)
      guess = eval(input('Enter 1 if my guess was high, -1 if low, and 0 if correct:'))
      while guess != -1 and guess !=1 and guess != 0:
        guess = eval(input('Enter 1 if my guess was high, -1 if low, and 0 if correct:'))
      count +=1
      if guess ==0:
        print()
        print("Thank you for playing the Guessing Game.")
        break
      elif count == 8:
        print("Either you guessed a number out of range or you had an incorrect entry.")
        break
      elif guess == -1:
        lo = mid + 1
      elif guess == 1:
        hi = mid - 1
  elif ready == 'n':
    print('Bye')
main()
