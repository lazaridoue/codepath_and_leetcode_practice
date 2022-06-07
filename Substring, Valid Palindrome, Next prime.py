import math
#Write a function that takes in two strings and returns true if the second string is substring of the first, and false otherwise.

def substring0(string1, string2):
  l1, l2 =len(string1), len(string2)
  if l2 == 0:
    return True
  elif l2>l1 or l1==0:
    return False
  else:
    if string2 in string2:
      return True
    else:
      return False

def substring1(string1, string2):
  l1, l2 =len(string1), len(string2)
  if l2 == 0:
    return True
  elif l2>l1 or l1==0:
    return False
  else:
    i,j=0,0
    while i < len(string1) and j < len(string2):
      if string1[i] == string2[j]:
        j+=1
        if j == len(string2)-1:
          return True
      i+=1
    return False


#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.        
        
def palindrome (s):
  s=s.lower()
  s=''.join(ch for ch in s if ch.isalnum())
  i,j=0,len(s)-1
  while i<j:
    if s[i]==s[j]:
      i+=1
      j-=1
    else:
      return False
  return True

#Given a number, return the next smallest prime number
#Note: A prime number is greater than one and has no other factors other than 1 and itself.
def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def next_prime(n):
  if n < 2:
     return 2
  while True:
    n+=1
    if is_prime(n)==True:
      return n
  