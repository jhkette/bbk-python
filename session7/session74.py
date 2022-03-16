# contains only uppercase letters
# im returning false if the string contains a number as well as this isn't a capital
def upperCase(str):
  try:
    flag = True
    for s in str:
      if s.isupper():
        pass
      else:
        flag = False
    return flag
  except:
    print("error")
print(upperCase('HKJ'))    
print(upperCase('HKJSAHDf'))
#contains at least one lowercase letter
def lowerCase(str):
  try:
    flag = False
    for s in str:
      if s.islower():
        flag = True    
    return flag
  except:
    print("error")
  
print(lowerCase('HHGGG'))
print(lowerCase('catDOG'))

# contains only digits or uppercase letters
def digitOrUpper(str):
  try:
    flag = True
    for s in str:
      if s.isupper() or s.isdigit():
        pass
      else:
        flag = False
    return flag
  except:
    print("error")
print(digitOrUpper('9FSASD'))    
print(digitOrUpper('HKhSAHDf'))
    

# contains all symbols (not letters or digits) 		isalnum()

def symbols(str):
  try:
    flag = True
    for s in str:
      if s.isalnum():
        flag = False
    return flag
  except:
    print("error")
print(symbols('123asdanji**'))
print(symbols('!!**'))

# starts with an uppercase letter and ends with a period 
def upperStop(str):
  try:
    if str[0].isupper() and str[-1] == '.':
      return True
    else:
      return False
  except:
    print("error")

print(upperStop('Hello.'))
print(upperStop('Hello there'))


"""
Write a function each that reads in a NON-EMPTY string and returns True whether it

contains only uppercase letters

contains at least one lowercase letter

contains only digits or uppercase letters

contains all symbols (not letters or digits) isalnum()

starts with an uppercase letter and ends with a period

For each function, find at least one case to make the function True and one case to make it False. Print results.
"""