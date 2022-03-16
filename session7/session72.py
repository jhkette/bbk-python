# define the squareColour() function
def squareColour(coords):
  if len(coords) != 2:
    print("error with input")
    return None
  l, num = coords
  letter = ord(l)
  if letter % 2 != 0 and num % 2 == 0 or letter % 2 == 0 and num % 2 != 0:
    return 'white'
  else:
    return 'black'
    
# define the main function, in which squareColour() is called
def main():
  try:
    coords = checkChessGrid()
    colour = squareColour(coords)
    strCoords = ''.join([str(item) for item in coords])
    return f"{strCoords} is {colour}"
  except:
    pass

def  checkChessGrid():
  string = input("please enter a two letter string: ")
  try:
    letter = string[0].lower() 
    number = int(string[1:])
    if letter <= 'h' and number >=1 and number <= 8:
      return [letter, number] 
    else:
      print('Error with input')
      return None
  except:
    print('Error with input')
    return None
    

print(main())

"""
Define a function squareColour() that takes in a list of length of 2

The first element of the list is a letter between 'a' to 'h'

The second element of the list is an integer between 1 to 8

It will return which colour the square has "black" or "white"

Define a main function

Call checkChessGrid() from Problem 7.2
Call the squareColour() function using the return of checkChessGrid()
Print out the square colour like g4 is white or d8 is black
Test cases:

"A1" - black

"b1" - white

"h5" - white

"u7" - error message

"9" - error message
"""