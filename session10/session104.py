def median(*args):
  try: #error check args to check they are numbers
    if len(args) == 0:
      print("Enter at least one number")
      return None
    # turn args from tuple into a list and assign to new_list
    new_list= list(args)  
    # sort list (sort only works with lists)
    new_list.sort()
    # floor division to get middle index
    index = len(new_list) //2 
    # if new_list is even we need to add the preceding item and divide by two
    if len(new_list) % 2 == 0:
      return (new_list[index] + new_list[index-1]) /2
    else:
      # else return the middle index
      return new_list[index]
  except:
    print("Error with input")
  

print(median(6, 3, 4, 1, 5)) # prints 4

print(median(6, 3, 4, 1, 5, 8)) # prints 4.5

print(median()) # prints "Enter at least one number" and None
