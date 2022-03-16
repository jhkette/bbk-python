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
"""
Write a function display a number triangle, given the height.

def numberTriangle(start, step, height):

start is the first number to fill in.

step is the step size.

The base is 2*height-1.

numberTriangle(1, 2, 8) is as shown.

1

3 5

7 9 11

13 15 17 19

21 23 25 27 29

31 33 35 37 39 41

43 45 47 49 51 53 55

57 59 61 63 65 67 69 71 <--- This is height, height = 8

73 75 77 79 81 83 85

87 89 91 93 95 97

99 101 103 105 107

109 111 113 115

117 119 121

123 125

127
"""