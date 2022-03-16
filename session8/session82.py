def readable(phoneNum):
  # error check
  if len(phoneNum) != 10:
    return "Phone number must be 10 digits long"
  # futher error check
  if not phoneNum.isdigit():
    return "Phone number must be all digits"
  else:
  # return f string with sliced phone num and hyphens/brackets
    return f"({phoneNum[:3]}){phoneNum[3:6]}-{phoneNum[6:]}" 

print(readable("4155551212")) # prints (415)555-1212
print(readable("5656391452")) # prints (565)639-1452
print(readable("5307343711")) # prints (530)734-3711
print(readable("R15551212P"))
print(readable("4155051212"))