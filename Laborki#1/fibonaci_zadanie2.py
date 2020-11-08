a=0
b=1
s=input()
s=int(s)
c=0
f=0
lista= [0, 1]
li=[0, 1] #lista sum prefiksowych
while f<s:
    l=len(li)
    if c%2==0:
        a=a+b
        f=a
        lista.append(f)
        li.append(f+li[l-1])
    else:
        b=b+a
        f=b
        lista.append(f)
        li.append(f+li[l-1])
    c+=1
#print(lista)   #debug
#print(li)  #debug
if s in lista:
    print("tak")
else:#jak nie to sprawdzam sumy prefiksowe
    h=0 #pozycja w liscie
    sum=0
    while li[h]<=s:
        h+=1
    g=li[h]
    #print(h)   #debug
    j=0
    for j in range(0,h):
        if sum == s:
            break
        sum=g-li[j]
        #print(sum) #debug
    if sum == s:
        print("tak")
    elif s in li:
        print("tak")
    else:
        print("nie")
#wydaje mi się że program sprawdza wszystkie podciągi spójne, chociaż mogło się tak zdarzyć że pewnie zapomniałam o jakimś jeszcze jednym warunku i całość nie bd działać dobrze :< ale złożoność taikego programu na pewno bd lepsza niż n^2 na dwafory jednak boje się że nie bd działało więc wysyłam bruta który mam nadzieję że zadziała.
