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