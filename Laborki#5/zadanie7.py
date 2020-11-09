#Zadanie 7.
#Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n x n wypełnioną liczbami naturalnymi.
#Dla danej tablicy należy napisać funkcję, która będzie zwracała wartość True w przypadku,
#gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość False w przeciwnym przypadku.
#Wymiar tablicy powinien być definiowany przez użytkownika.

import random as generuje

tab=[]
'''
while 1:
    try:
        n=int(input("Prosze wprowadzic wymiar tablicy: "))
        tab=[[generuje.randint(0,3) for i in range(n)] for j in range(n)]
        break
    except:
        print("To nie jest liczba naturalna, prosze podac n jeszcze raz")
        continue
'''

#moje przyklady :>
n=1
tab=[[0,5,6,7,8],
     [9,3,2,0,4],
     [2,5,3,7,8],
     [9,0,0,0,1],
     [6,7,9,8,0]]

tab=[0]
'''
   k = 1,1,1,1,1
1    [[0,5,6,7,8],
1     [9,3,2,0,4],
1     [2,5,0,7,8],
1     [9,0,0,0,1],
1     [6,7,9,8,0]]
w
'''

for wiersz in tab:
    print(wiersz)

#[wiersz][kolumna]
w=[0]*n # czy w wierszu jest jakies zero jak tak=1
k=[0]*n # czy w kolumnie jest jakies zero jak tak=1
print()

if len(tab)==1:
    if tab[0]==0:
        w[0]=1
        k[0]=1
else:
    for wiersz in range(n):
        for kolumna in range(n):
            if tab[wiersz][kolumna]==0:
                k[kolumna]=1
                #print(kolumna)
                w[wiersz]=1
                #print(wiersz)

print("kolumna")
print(k)
print("wiersz")
print(w)
print()

if 0 in (w + k):
    print(False)
else:
    print(True)
