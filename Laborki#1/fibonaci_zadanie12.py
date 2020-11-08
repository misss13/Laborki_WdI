a=0
b=1
n=49#liczba ilosci liczb ciagu fibbonaciego
c=0
f=0
li=[0,1]
while c<n:
    if c%2==0:
        a=a+b
        f=a
        li.append(f)
    else:
        b=b+a
        f=b
        li.append(f)
    c+=1
for i in range(1,len(li)-1,2):
    print(li[i]/li[i+1])
print("calosc staje się coraz lepszym przyblizeniem zolotej liczby")
