"""I'm working on the assumption that this function is only
meant to add commas to digits - as the test cases suggest - so I am returning false if it is not a digit"""

def addComma(string):
  if string.isdigit():
    start = 0
    step = 3
    final_string = ""
    length = len(string)
    while step < length:
      final_string += string[start:step] +',' 
      step +=3
      start+=3 
    final_string += string[start:]
    return final_string
  else:
    print('Please add a number string')
    return False
      
print(addComma("458")) # returns and prints"458"
print(addComma("45876")) # returns and prints"458,76"
print(addComma("458763")) # returns and prints"458,763"
print(addComma("4587632")) # returns and prints "458,763,2"
print(addComma("1000000")) # returns and prints "458,763,2"