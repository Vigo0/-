def ab(a):
    if a<0:
        return-a
    else:
        return a


    
def gcd (a,b):
    a = ab(a)
    b = ab(b)
    if a*b ==0:
        return a+b
    else:
        if a>b:
           return gcd(a%b,b)
        else:
           return gcd(a,b%a)
print("gcd(-30,33)=",gcd(-30,33))


