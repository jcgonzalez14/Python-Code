#  File: CreditCard.py

#  Description: Homework#8

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/9/16

#  Date Last Modified: 4/9/16

def sum_digits (n):
  sum_num = 0
  while (n > 0):
    sum_num = sum_num + (n % 10)
    n = n // 10
  return sum_num

def main():
  card = eval (input ('Enter 15 or 16-digit credit card number:'))
  lst = [int(i) for i in str(card)]
  if len(lst) == 15 or len(lst) == 16:
    if len(lst) == 16:
      odd = lst[::2]
      even = lst[1::2]
    else:
      even = lst[::2]
      odd = lst[1::2]
    b =[]
    for i in range(len(odd)):
      b.append(sum_digits(odd[i]*2))
    if ((sum(b) + sum(even)) % 10) == 0:
      print("Valid", end =' ')
      if lst[0] == 3 and (lst[1] == 4 or lst[1]==7):
        print("American Express credit card number")
      elif lst[0] == 6 and ((lst[1] == 5) or (lst[1] == 4 and lst[2] == 4) or (lst[1] == 0 and lst[2] == 1 and lst[3] ==1)):
        print("Discover credit card number")
      elif lst[0] == 5 and (lst[1]==0 or lst[1]==1 or lst[1]==2 or lst[1]==3 or lst[1]==4 or lst[1]==5):
        print("MasterCard credit card number")
      elif lst[0] == 4:
        print("Visa credit card number")
      else:
        print("credit card number")
      
    else:
      print("Invalid credit card number")
  else:
      print("Not a 15 or 16-digit number")

main()
