def gcd (a,b):
    if a < 0 :
        a*= -1
    if b < 0 :
        b*= -1
    if a*b ==0:
        return a+b
    else:
        if a>b:
           return gcd(a%b,b)
        else:
           return gcd(a,b%a)
print("gcd(-30,33)=",gcd(-30,33))



