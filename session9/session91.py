def numberTriangle(start, step, height):
  num = 1
  for i in range(0, height+1):
    for j in range(1, i+1):
      print(num, end=" ")
      num += step 
    print()
  for i in range( height+1, 0, -1):
    for j in range(1, i-1):
      print(num, end=" ")
      num += step 
    print()



numberTriangle(1, 2, 8)