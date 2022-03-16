# No need to define a function
nums = [] #initialise nums variable
i = 0 #counter variable
while i <5: # while loop which asks the user to enter a
# number 5 times
  x = int(input("Please enter a number: "))
  i+= 1
  nums.append(x)

print(nums)
last=input("Do you want to keep the last number? y/n: ")
# remove last number of last == n
if last == 'n':
  nums.pop()
  print(nums)
else:
  print(nums)

minNum = nums[ 0 ]
for a in nums:
    if a < minNum:
        minNum = a
# use list comprehension to get a new list without smallest number
finalnums = [n for n in nums if n != minNum]
#print final list of numbers
print(finalnums)
  
"""
Create an empty list called nums.

Ask the user to enter 5 numbers.

After each number is entered, add it to the end of nums and display the list.

Once they have entered all 5 numbers, ask them if they still want the last number they entered to be saved. If they say “no”, remove the last item from the list.

Display the list of numbers.

Remove the smallest in the remaining list.

If there are multiple smallest values, remove them all.

Test Cases

Run the following three test cases:

4, 4, 4, 5, 4 and "y" # returns [5]

3, 4, 4, 6, 9 and "n" # returns [4, 4, 6]

3, 3, 4, 6, 3 and "y" # returns [4,6]

4, 4, 4, 4, 4 and "y" # returns []
"""