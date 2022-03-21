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

def readInteger():
  user_number = ' '
  while user_number.isdigit() == False or user_number[-1] == '0':
    user_number = input("Please enter a number: ")
    if user_number.isdigit() and int(user_number) > 0:
      if user_number[-1] != '0':
        return user_number
      else:
        print("Last digit must not be 0")
    else:
      print("Input must be a positive integer")
    

def main():
  number = readInteger()
  reversed = number[::-1]
  final = addComma(reversed)
  return final

print(main())

