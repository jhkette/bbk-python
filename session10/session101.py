def discount(*args):
  try: # error check the - args need to be numeric
    if len(args) >=5 and sum(args) >= 60: # discount check
      print("Congrats! Discount applies!")
      return round(sum(args) * 0.8, 2) # return sum args and discount
    else: 
      print("Sorry, no discount.") # else no discount
      return sum(args) # simply return sum of the args
  except:
    print("Error with input")


print(discount(56, 35)) #91

print(discount(5, 6, 2, 4, 7)) #24

print(discount(12, 12, 12, 12, 12)) #48.0

print(discount(12, 12, 12, 12, 11)) #59

print(discount(60)) #60

print(discount(0)) #0