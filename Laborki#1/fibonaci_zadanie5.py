koncowystan="nie"
a=0
b=1
n=input()
n=int(n)
c=0
f=0
li=[0,1]
while f<n:
    if c%2==0:
        a=a+b
        f=a
        li.append(f)
    else:
        b=b+a
        f=b
        li.append(f)
    c+=1
l=len(li)
#print(li)
d=0
for d in range(1,l):
    if n%(li[d])==0:
        if (n//(li[d])) in li:
            #print("tak")
            koncowystan="tak"
            break
print(koncowystan)
