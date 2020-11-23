#Na szachownicy o wymiarach 100 na 100 umieszczamy 𝑁 gońców (𝑁 < 100). Położenie gońców jest opisywane przez tablicę
#𝑑𝑎𝑛𝑒 = [(𝑤1,𝑘1),(𝑤2,𝑘2),(𝑤3,𝑘3),...(𝑤𝑁 ,𝑘𝑁 )]. Proszę napisać funkcję, która zwróci położenie gońców wzajemnie się szachujących.
#Do funkcji należy przekazać położenie gońców. Należy zwizualizować rozkład gońców na szachownicy.
#Test:
#1.Przypadek, w którym nie występuje szachowanie.
#2.Szachują się dwa gońce.
#3.Szachuje się więcej niż dwa gońce.

import numpy as np
from tabulate import tabulate

m=10
szachownica=[[' ' for i in range(m)] for j in range(m)]
sza=[['0' for i in range(m)] for j in range(m)]
headers=[*range(m)]

while 1:
    try:
        n=int(input("Prosze podac ilosc goncow: "))
    except ValueError:
        print('To nie liczba!')
    else:
       if 1 <= n < m:
           break
       else:
           print('Liczba spoza zakresu')
for i in range(n):
    print("Zmienna nr: %d" %(i+1))
    while 1:
        try:
            wier=int(input("Proszę podac wiersz: "))
            kol=int(input("Proszę podac kolumne: "))
        except ValueError:
            print('To nie liczba!')
        else:
           if (0 <= kol < m) and (0 <= kol < m):
               break
           else:
               print('Liczba spoza zakresu')
    szachownica[wier][kol]="G"
    sza[wier][kol]=(1+i)

szachownica[8][0]="G"
szachownica[9][1]="G"
szachownica[5][1]="G"
szachownica[6][2]="G"
szachownica[7][3]="G"
sza[9][1]=2
sza[5][1]=3
sza[6][2]=4
sza[7][3]=5
sza[8][0]=6

for i in range(m):
    szachownica[i].insert(0,str(i))
print(tabulate(szachownica, headers, tablefmt="grid"))
for i in sza:
    print(i)

def gonce(sza,m,szachownica):
    zbijajace=[]

    matrix=np.array(sza)
    diags = [matrix[::-1,:].diagonal(i) for i in range(-(m-1),m)]
    diags.extend(matrix.diagonal(i) for i in range((m-1),-m,-1))
    for n in diags:
        a=0
        q=n.tolist()
        print(q) #mozna ukryc
        #print(q[0])
        for i in range(len(q)):
            if q[i] != '0':
                a+=1
        if a>=2:
            for j in range(len(q)):
                if q[j] != '0':
                    zbijajace.append(q[j])
    #print(zbijajace)
    zbijajace = list( dict.fromkeys(zbijajace)) #wyrzucam powtorzenia
    print("Gonce wprowadzone ktore bija")
    print(zbijajace)
    #print(matrix)
    return szachownica,matrix,zbijajace

sz,matrix,zbijajace=gonce(sza,m,szachownica)

for i in range(m): #wiersze
    for j in range(m): #kol
        if matrix[i][j] in zbijajace:
            print("wiersz %d kolumna %d " %(i ,j))
            szachownica[i][j+1]="X"
print(tabulate(sz, headers, tablefmt="grid"))

def wypis(sza,h):
    for i in sza:
        for j in i:
            if j==" ":
                print("O",end="")
            elif j=="X":
                print("X",end="")
            elif j in str(h):
                print("",end="")
            else:
                print("G",end="")
        print("")

wypis(szachownica,headers)
