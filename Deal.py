#  File: Deal.py

#  Description: Homework#3

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 33375

#  Date Created: 3/2/16

#  Date Last Modified: 3/5/16

import math
import random

def main():
  play = eval (input ("Enter number of times you want to play: "))
  counter = 1
  win = 0
  print()
  print("  Prize      Guess       View    New Guess")
  
  while counter <= play:
    guess = random.randint(1,3)
    prize = random.randint(1,3)
    view = random.randint(1,3)
    while view == guess or view == prize:
      view = random.randint(1,3)
    newGuess = random.randint(1,3)
    while newGuess == guess or newGuess == view:
      newGuess = random.randint(1,3)
    print("   ", prize, "        ", guess, "        ", view,"        ", newGuess)
    if newGuess == prize:
       win +=1
    counter +=1

  loss = (1 - (win/play))
  
  print()
  print("Probability of winning if you switch =", '{0:.2f}'.format(win/play))
  print("Probability of winning if you do not switch =", '{0:.2f}'.format(round(loss,2)))
main()

