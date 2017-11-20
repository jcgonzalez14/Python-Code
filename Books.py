#  File: Books.py

#  Description: Homework#8

#  Student Name: Julio Gonzalez

#  Student UT EID: jcg3245

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/21/16

#  Date Last Modified: 4/28/16

# Create word dictionary from the comprehensive word list
import string

book_dict = {}
def create_word_dict ():
  # open file for reading
  in_file = open ("./words.txt", "r")

  for line in in_file:
    line = line.strip()
    book_dict[line] = 1

# Removes punctuation marks from a string
def parseString (st):
  s = ''
  for ch in st:
    if ch.isalpha() or ch.isspace():
      s += ch
    else:
      s += ''
  return(s)

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
  # open the book
  book = open (file, "r")

  # create an empty set for unique words
  word_set = set()

  # create a dictionary for the word frequency
  word_dict = {}

  # track the total number of words
  total_words = 0

  # read the book
  for line in book:
    line = line.strip()
    line = parseString(line)

    word_list = line.split()

    # add words to the set and to the dictionary
    for word in word_list:
      word_set.add (word)
      total_words += 1

      # add word to the frequency dictionary
      if word in word_dict:
        word_dict [word] = word_dict[word] + 1
      else:
        word_dict[word] = 1

  # close the file
  book.close()
  
  capital_letters = []
  for key in word_dict:
      if key[0].isupper():
        capital_letters.append(key)

  for word in capital_letters:
    if word.lower() in word_dict:
      word_dict[word.lower()] += word_dict[word]
      
    elif word.lower() in book_dict:
      word_dict[word.lower] = 1
    else:
      del word_dict[word]

  return word_dict
      

      
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):

  a1 = len(freq1.keys())
  b2 = len(freq2.keys())

  set1 = set (freq1.keys())
  set2 = set (freq2.keys())
  a = len (set1 - set2)
  b = len (set2 - set1)

  total_words1 = 0
  for key in freq1:
    total_words1 += freq1[key]

  total_words2 = 0
  for key in freq2:
    total_words2 += freq2[key]

  relative_1 = 0
  for key in freq1:
    if key not in freq2:
      relative_1 += freq1[key]

  relative_2 = 0
  for key in freq2:
    if key not in freq1:
      relative_2 += freq2[key]

  percent1 = (relative_1/total_words1)*100
  percent2 = (relative_2/total_words2)*100

  set1 = set (freq1.keys())
  set2 = set (freq2.keys())
  a = len (set1 - set2)
  b = len (set2 - set1)

  

  print(author1)
  print("Total distinct words =", a1)
  print("Total words (including duplicates) =", total_words1)
  print("Ratio (% of total distinct words to total words) = ", (a1/total_words1)*100)
  print()
  print(author2)
  print("Total distinct words =", b2)
  print("Total words (including duplicates) =", total_words2)
  print("Ratio (% of total distinct words to total words) = ", (b2/total_words2)*100)
  print()
  print(author1+" used "+ str(a)+" words that "+author2+" did not use.")
  print("Relative frequency of words used by "+author1+" not in common with "+author2+" = "+str(percent1))
  print()
  print(author2+" used "+ str(b) +" words that "+author1+" did not use.")
  print("Relative frequency of words used by "+author2+" not in common with "+author1+" = "+str(percent2))

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)


  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
