#  File: GuessingGame.py

#  Description: Homework#8

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/15/16

#  Date Last Modified: 4/16/16

def main():
  # open file for reading
  in_file = open ("grid.txt", "r")

  # read the dimension of the grid
  dim = in_file.readline()
  dim = dim.strip()
  dim = int (dim)

  # create an empty grid and populate it
  grid = []

  for i in range (dim):
    row = in_file.readline()
    row = row.strip()
    row = row.split()
    for j in range (dim):
      row[j] = int (row[j])
    grid.append (row)

   # print (grid)

  # close the file
  in_file.close()

  # read each row in blocks of four
  highest = 0
  for row in grid:
    for i in range (0, len(row) - 3):
      product = 1
      for j in range (i, i + 4):
        product = row[j]*product
      if product > highest:
        highest = product

  # read each column in blocks of four
  for j in range (dim):
    for i in range (0, dim - 3):
      trust = 1
      for k in range (i, i + 4):
        trust = grid[k][j]*trust
      if trust > highest:
        highest = trust
  
  # read along major diagonal going L to R in blocks of four

  for n in range(3, dim):
    for i in range (dim - n):
      dick = 1
      for j in range (i, i + 4):
        dick = grid[j+(n-3)][j]*dick
      if dick > highest:
        highest = dick
   
  for n in range(3, dim):
    for i in range (dim - n):
      tit = 1
      for j in range (i, i + 4):
        tit = grid[j][j+(n-3)]*tit
      if tit > highest:
        highest = tit
  
  # read along major diagonal going R to L in blocks of four                    
  for n in range(3, dim):
    for i in range (dim - n):
      no = 1
      for j in range (i, i + 4):
        no = grid[j][dim - (n-2) - j]*no
      if no > highest:
        highest = no

  for n in range(3, dim):
    for i in range (dim - n):
      how = 1 
      for j in range (i, i + 4):    
        how = grid[j + (n-3)][dim - 1- j]*how
      if how > highest:
        highest = how
  print("The greatest product is {}.".format(highest))
  

main()
