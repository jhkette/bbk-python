"""
sumBigEven is a function that adds even numbers over 10.
First I am returning -1 if the length of the list is -1.
Then I am looping through nList and  adding an if statement which adds to total if certain conditions are met. Then I return the total value. I also inlcude basic error checking - so if an incorrect value is entered the error is handled gracefully.  
"""
def sumBigEven(nList):
  try: #error checking
    if len(nList) == 0: 
      return -1
    total = 0
    for n in nList:
      if n > 10 and n % 2 == 0:
        total += n
    return total
  except:
    print("Wrong value entered")