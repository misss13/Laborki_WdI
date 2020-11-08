
czytakczynie="nie"
a=0
b=1
s=input()
s=int(s)
c=0
f=0
lista= [0, 1]
while f<s:
    if c%2==0:
        a=a+b
        f=a
        lista.append(f)
    else:
        b=b+a
        f=b
        lista.append(f)
    c+=1
print(lista)   #debug
for i in lista:
    sum=0
    for j in range(i,len(lista),1):
        sum+= lista[j]
        if sum == s:
            czytakczynie="tak"
            break
print(czytakczynie)
