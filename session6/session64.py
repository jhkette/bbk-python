# Define the function
def calSum(lst):
  sumAll = 0 #define sumAll variable
  for i,n in enumerate(lst): #loop through lst with index and number
  #if the index is divisible by two add - else - from sumAll
    if i % 2 == 0:
      sumAll += n
    else:  
      sumAll -= n
  return sumAll



# Call the function four times and print out the results
print(calSum([]))
print(calSum([4]))
print(calSum([3, -8]))
print(calSum([1, 4, 9, 16, 9, 7, 4, 9, 11]))

"""
•Write a function to calculate and return the alternating sum of all elements in a list.

For example, if the list is [1, 4, 9, 16, 9, 7, 4, 9, 11], then it computes

1 – 4 + 9 – 16 + 9 – 7 + 4 – 9 + 11 = -2

Test Cases:

Run three tests:

[] # should return 0

[4] # should return 4

[3, -8] # should return 11

[1, 4, 9, 16, 9, 7, 4, 9, 11] # should return -2
"""