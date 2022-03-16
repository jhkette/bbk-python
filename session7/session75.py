# No need to define a function
password = "123456"
correct = False
num = 0
while num < 3 and correct == False:
  attempt = input("Please enter your password: ")
  if attempt == password:
    correct = True
    print("Password correct! Welcome!")
  else:
    num += 1
    print("Invalid input")
if num == 3:
  print("Too many attempts. Account locked.")

"""
Preset the password to be, e.g., "123456"

A user is prompt to enter the password

"Please enter your password: "

But s/he has only at most 3 chances

If the password is correct, print out "Password correct! Welcome!"

If the password is incorrect, print out "Invalid input"

If all 3 attempts failed, then print out "Too many attempts. Account locked."

Test cases:

123456

12, 123456

12, 1234, 123456

12, 123, 1234

Expected Output:

"Password correct! Welcome!"

"Invalid input", "Password correct! Welcome!"

"Invalid input", "Invalid input", "Password correct! Welcome!"

"Invalid input", "Invalid input", "Invalid input", "Too many attempts. Account locked."
"""