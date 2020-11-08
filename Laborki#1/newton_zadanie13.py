epsi=0.000001
a=input()
a=int(a)
b=a/3
c=0
d=0
while abs(b-c) >= epsi:
    if d%2==0:
        c=((2*b+a/(b**2))/3)
        #print(c)
    else:
        b=((2*c+a/(c**2))/3)
        #print(b)
    d+=1
print(b)
print(c)
#1/3((2)xk+A/xk^2)
