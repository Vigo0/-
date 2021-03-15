import math
import numpy
def gcd (a,b):
  b=abs(b)
  a=abs(a)
  if a*b ==0:
      return a+b
  else:
      if a>b:
          return gcd(a%b,b)
      else:
          return gcd(a,b%a)
print("gcd(-30,33)=",gcd(-30,33))



