#'''
import random

while 1:
    try:
        n= int(input("Prosze podac n: "))
        break
    except:
        print("To nie jest liczba naturalna, prosze podac n jeszcze raz")
        continue
lista=[]
for i in range(n):
    a= random.randint(0,100) #zakres liczb losowych 0 - 100
    #print(a) #debug
    lista.append(a)
#print(lista) #debug #koniec losowania liczb
#'''
#lista=[1,2,3,4,5,4,15,20,20,60,61,62,63,64,65]

print(lista)
l=len(lista)
ma=0 #maksymalna dlugosc podciagu
sp=0 #aktualna dlugosc znalezionego podciagu
po=0 #ostateczny poczatek do ktorego bd dodawac sp
p=0 # altualny poczatek
for i in range(1,l):
    if lista[i]>lista[i-1]:
        sp+=1
        print(lista[p:(p+sp)]) #debug
        if sp>ma:
            ma=sp
            po=p
    else:
        p=i
        sp=1
print(lista[po:(po+ma)])
print(ma)
#wysylam bo sie pomylilam i to najpierw napisalam :<
