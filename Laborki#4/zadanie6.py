#Zadanie 6. Prosze napisac funkcje, ktora dla N-elementowej tablicy wypelnionej liczbami naturalnym wyznacza
#dlugosc najdluzszego, spojnego podciagu arytmetycznego.
#'''

import random
from math import inf

while 1:
    try:
        n= int(input("Prosze podac n: "))
        break
    except:
        print("To nie jest liczba naturalna, prosze podac n jeszcze raz")
        continue
lista=[]
for i in range(n):
    a= random.randint(0,4) #zakres liczb losowych 0 - 4 najbardziej widac ze dziala
    #print(a) #debug
    lista.append(a) #debug #koniec losowania liczb
#'''
#lista=[1,2,3,4,5,4,15,20,20,60,62,64,66,68,70]
#lista=[1,3,5,7,20,18,16,14,12,10]
#lista = [0, 0, 0, 3, 1, 3, 2, 2, 4, 4, 1, 4, 0, 4, 2, 4, 3, 0, 0, 3, 3, 0, 1, 3, 4, 0, 4, 1, 0, 2, 1, 3, 4, 1, 3, 3, 1, 3, 4, 3, 1, 0, 3, 1, 4, 0, 3, 0, 1, 1, 3, 1, 0, 4, 3]
#3lista=[1,2,3,1,2,3,4,1,2,3,4,5]

print(lista)
l=len(lista)
ma=2 #maksymalna dlugosc podciagu
sp=2 #aktualna dlugosc znalezionego podciagu
po=0 #ostateczny poczatek do ktorego bd dodawac ma
p=0 # aktualny poczatek
r=-inf #aktualna reszta
for i in range(1,l):
    if (lista[i]-lista[i-1]) == r:
        # print(str(lista[i-1]) + " " + str(lista[i]) + " " + str(lista[i]-lista[i-1]) + " " + str(sp)) #debug
        sp+=1
        print(lista[p:(p+sp)]) #debug
        if sp>ma:
            ma=sp
            po=p
    else:
        p=i-1
        sp=2
        r=lista[i]-lista[i-1]
print(lista[po:(po+ma)])
print(ma)
