def mean(*args):
  try: # error check - to check apprpriate values entered
    if len(args) == 0: # check if an args added
      print("Enter at least one number.")
      return None
    else:
      # return sum divided by number of args
      return sum(args) / len(args)  
  except:
    print('Error with arguments added')

print(mean())

# prints "Enter at least one number."

# prints None

print(mean(0))

# prints 0.0

print(mean(1))

# prints 1.0

print(mean(3,4,5))

# prints 4.0