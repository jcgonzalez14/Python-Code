#  File: Benford.py

#  Description: Homework#8

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/22/16

#  Date Last Modified: 4/20/16

def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0
  pop_freq ['7'] = 0
  pop_freq ['8'] = 0
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()
  total_num = 0
  b =[]
  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    b.append(pop_num[0])
    

    # make entries in the dictionary
  for i in b:
    if i in pop_freq:
            pop_freq[i] = pop_freq[i] + 1
            total_num +=1

  # close the file
  in_file.close()
  

  # write out the result
  all_numbers = list (pop_freq.keys())
  all_numbers.sort()
  print("Digit	Count	  %")
  for i in all_numbers:
      percentage = round((pop_freq[i] / total_num)*100, 1)
      print(i+ '       '+'%-6s'% str(pop_freq[i]), end = '    ')
      print(str(percentage))
##      print(i+"        " + str(pop_freq[i])+"     "+ str(percentage))
  
main()
