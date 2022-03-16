def printFourPowerTable(number, power):
  header=""
  for i in range (1, power+1):
    header+= '{:^9}'.format('x^'+str(i))
  print(header)
  print('-' * len(header))
  numbers = ""
  for i in range(1, number +1):
    for j in range(1,power+1):
      numbers += '{:^9}'.format(str(pow(i,j)))
    numbers +="\n"
  return numbers
      
   
print(printFourPowerTable(10, 5))


"""
Write a function

def printFourPowerTable(number):

This function will print out the 4 power table for (1 to number).

For example,

printFourPowerTable(10) prints

    x^1        x^2        x^3         x^4
    x^1        x^2        x^3         x^4
        1            1            1            1
        2            4            8          16
        3            9           27         81
        4          16           64       256
        5          25         125       625
        6          36         216     1296
        7          49         343     2401
        8          64         512     4096
        9          81         729     6561
      10        100       1000   10000
        1            1            1            1
        2            4            8          16
        3            9           27         81
        4          16           64       256
        5          25         125       625
        6          36         216     1296
        7          49         343     2401
        8          64         512     4096
        9          81         729     6561
      10        100       1000   10000

"""