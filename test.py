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
    

print(readInteger())