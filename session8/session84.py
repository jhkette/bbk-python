def isPalindrome(content):
  #remove punctuation and whitespace
  final =  "".join([c for c in str(content) if c not in ('!','.',',',"'", " ")]).lower()
  # check for pallindrome by comparing to reversed string
  if str(final) == final[::-1]:
    return True
  else:
    return False
 
print(isPalindrome(121)) #True
print(isPalindrome("deed")) # True
print(isPalindrome("Rotor")) # True
print(isPalindrome("Madam, I'm Adam.")) # True
print(isPalindrome("friend")) # False
print(isPalindrome(1234))# False
