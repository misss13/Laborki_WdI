epsi=0.000001
a=input()
a=int(a)
b=a/2
c=0
d=0
while abs(b-c) >= epsi:
    if d%2==0:
        c=((b+a/b)/2)
        #print(c)
    else:
        b=((c+a/c)/2)
        #print(b)
    d+=1
print(b)
#print(c)
