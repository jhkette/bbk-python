import random

def randSwap(string):
  try:
    length = len(string) #length of string input
    if length < 2: #error checking
      print("String length should be at least 2")
      return None
    # to avoid making this problem more complex i am ensuring
    # j is at least one greater than i
    i = random.randint(0, length -2) #i position
    j = random.randint(i+1, length -1) #j position
    # split string elements into list, join and return
    return ''.join([string[:i], string[j], string[i+1:j], string[i], string[j+1:]])
  except:
    print("Invalid input")

print(randSwap(""))
print(randSwap("s"))
print(randSwap("st"))
print(randSwap("string"))

# string[:i] up to i position
# string[j] and string at j position
# string[i+1:j] i +1 so one above from where 'i' was. up to - but not including- j
# string[i] add string i where string j would have been


"""
Translate the following pseudocode for randomly permuting the characters in a string into a Python program.

Read a word

Repeat len(word) times

Pick a random position i in the word, but not the last position

Pick a random position j > i in the word

Swap the letters at positions i and j

Print the word

Make the function randint() accessible to your program by using the code

import random

If a, b are integers such that a <= b, then random.randint(a, b) returns a random integer r such that a <= r <= b (both inclusive).

•To swap the letters, randomly select indices i and j.

first is the part before i

middle is the part between i and j

last is the part after j

Then replace the string with

first + word[j] + middle + word[i] + last

•To use string slicing to help you code. Make sure the input is at least 2-character long

•Code to generate i and j:

import random

length = len(word)

i = random.randint(0, length-2)

j = random.randint(i+1, length-1)

•Test cases:

print(randSwap(""))

# prints String length should be at least 2.

# prints None

print(randSwap("s"))

# prints String length should be at least 2. # prints None

print(randSwap("st"))

# prints ts

print(randSwap("str"))

# prints a random combination of str

print(randSwap("string"))

# prints a random combination of string
"""