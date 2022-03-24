def mode(*args):
  try: # error checking to see if appropraite args are added
    if len(args) == 0: # if no args return none 
      print("Enter at least one number")
      return None
    # create a dictionary using the args as keys
    hash_map = dict.fromkeys(args, 0)
    for a in args: # loop through args
      # add  1 to dict value
        hash_map[a] += 1 
    # return the key with the max value from the hash_map 
    return max(hash_map, key=hash_map.get)
  except:
    print("Incorrect argument added")
    
print(mode(6, 3, 9, 6, 6, 5, 9, 3)) # prints 6

print(mode(3, 3, 3, 4, 4, 4, 5)) # prints 3

print(mode()) # prints "Enter at least one number" and None
#another test to check
print(mode(3, 3, 3, 4, 4, 4, 5,5,5,5,5,5,5)) # prints 3