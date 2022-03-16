"""I'm using a two pointer search style algorithm
to solve this problem efficently. Because we need to find the point in the list where the number is greater than the preceding element but less than the following element (if a following element exits) """

def sortInsert(nums, numAdd) -> int:
    low, high = 0, len(nums)-1 #find low high
    while low <= high: # low greater than high
        mid = low + (high-low)//2 # get middle - this will be index to insert number
        if nums[mid] < numAdd: # if nums greater than numAdd mid+1
            low = mid+1
        else:
            high = mid-1 # if nums less than numAdd mid-1
    nums.insert(low, numAdd)
    return nums



print(sortInsert([0,2,4,6], 0))

print(sortInsert([0,2,4,6], 1))

print(sortInsert([0,2,4,6], 3))

print(sortInsert([0,2,4,6], 4))

print(sortInsert([0,2,4,6], 6))

print(sortInsert([0,2,4,6], 7))

"""
Suppose that sortedIntList is a sorted list of integers.

Write a function to insert a new value newInt into its proper position without calling the sort() function.

input: sortedIntList and newInt

output: the updated sortedIntList

For instance:

sortedIntList is [2, 6, 9, 19]

newInt is 16

updated sortedIntList is [2, 6, 9, 16, 19]

Test Cases

print(sortInsert([0,2,4,6], 0))

print(sortInsert([0,2,4,6], 1))

print(sortInsert([0,2,4,6], 3))

print(sortInsert([0,2,4,6], 4))

print(sortInsert([0,2,4,6], 6))

print(sortInsert([0,2,4,6], 7))

Expected output:

# Returns [0, 0, 2, 4, 6]

# Returns [0, 1, 2, 4, 6]

# Returns [0, 2, 3, 4, 6]

# Returns [0, 2, 4, 4, 6]

# Returns [0, 2, 4, 6, 6]

# Returns [0, 2, 4, 6, 7]
"""