epsi=0.00001
pierwias=2**(1/2)
print(pierwias)
a=1
b=2
c=(a+b)/2
y=((c**2)-2)
while abs(pierwias-c)>=epsi:
    if y>0:
        b=c
        print(b)
    else:
        a=c
        print(a)
    c=(a+b)/2
    y=((c**2)-2)
