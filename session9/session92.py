def printPossiblePairs(number):
  if isinstance(number, int):
      string = ""
      for i in range(1, number+1):
        for j in range(1, number+1):
          print(f"({i},{j})", end="")
        print()  
      print(string)
  else:
    print("Non integer provided")
       

printPossiblePairs(4)
"""
Write a function called printPossiblePairs that accepts one argument and prints every possible pair of positive numbers in which both numbers are no more than the argument.

You should print each pair with a comma and a space separating the two numbers.

For example, printPossiblePairs(4) should print every possible pair of positive numbers in which both numbers are no more than 4 in the following order.

Display n results in a row, where n is the argument (in this case n = 4).

(1, 1) (1, 2) (1, 3) (1, 4)

(2, 1) (2, 2) (2, 3) (2, 4)

(3, 1) (3, 2) (3, 3) (3, 4)

(4, 1) (4, 2) (4, 3) (4, 4)
"""