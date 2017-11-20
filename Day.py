#  File: Day.py

#  Description: Homework#2

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 33375

#  Date Created: 1/30/16

#  Date Last Modified: 2/5/16

def main():
  # prompt user to enter year
  year = eval (input ("Enter year: "))

  while ((year < 1900) or (year > 2100)):
    year = eval (input ("Enter year: "))

  # prompt the user to enter month
  month = eval (input ("Enter month: "))

  while ((month < 1) or (month > 12)):
    month = eval (input ("Enter month: "))

  # prompt the user to enter day
  day = eval (input ("Enter day: "))

  # determine if the year is a leap year or not
  is_leap =  (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))

  # compute number of days in a month
  num_days = 0
  if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or \
  (month == 8) or (month == 10) or (month == 12)):
    num_days = 31
  elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
    num_days = 30
  elif (month == 2):
    num_days = 28
    if (is_leap):
      num_days = 29

  while ((day < 1) or (day > num_days)):
    day = eval (input ("Enter day: "))

  # compute the day of the week
  if (month==3):
    a=1
  elif(month==4):
    a=2
  elif(month==5):
    a=3
  elif(month==6):
    a=4
  elif(month==7):
    a=5
  elif(month==8):
    a=6
  elif(month==9):
    a=7
  elif(month==10):
    a=8
  elif(month==11):
    a=9
  elif(month==12):
    a=10
  elif(month==1):
    a=11
    year = year - 1
  elif(month==2):
    a=12
    year = year - 1

  b = day
  c = year%100
  d = year//100
  
  w = (13 * a - 1 ) // 5 
  x = c // 4
  y = d // 4
  z = w + x + y + b + c - 2 * d
  r = z % 7 
  r = (r + 7) % 7

  print()

  #print the day of the week
  if (r==0):
    print("The day is Sunday.")
  elif (r==1):
    print("The day is Monday.")
  elif (r==2):
    print("The day is Tuesday.")
  elif (r==3):
    print("The day is Wednesday.")
  elif (r==4):
    print("The day is Thursday.")
  elif (r==5):
    print("The day is Friday.")
  elif (r==6):
    print("The day is Saturday.")

main()
