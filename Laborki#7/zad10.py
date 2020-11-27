#Na szachownicy o wymiarach 100 na 100 umieszczamy 𝑁 gońców (𝑁 < 100). Położenie gońców jest opisywane przez tablicę
#𝑑𝑎𝑛𝑒 = [(𝑤1,𝑘1),(𝑤2,𝑘2),(𝑤3,𝑘3),...(𝑤𝑁 ,𝑘𝑁 )]. Proszę napisać funkcję, która zwróci położenie gońców wzajemnie się szachujących.
#Do funkcji należy przekazać położenie gońców. Należy zwizualizować rozkład gońców na szachownicy.
#Test:
#1.Przypadek, w którym nie występuje szachowanie.
#2.Szachują się dwa gońce.
#3.Szachuje się więcej niż dwa gońce.

from random import randint
import matplotlib.pyplot as plt

m=10
dane=[(randint(0, m-1), randint(0, m-1)) for i in range(m)]
dane=list(dict.fromkeys(dane))
x=[i[0] for i in dane]
y=[i[1] for i in dane]

print(dane)
print(x)
print(y)
praw=[]
lew=[]
przekatn_prawo=[i[0]-i[1] for i in dane]
print(przekatn_prawo)
przekatn_lewno=[j[0]+j[1] for j in dane]
print(przekatn_lewno)

l = list( dict.fromkeys(przekatn_lewno))
p = list(dict.fromkeys(przekatn_prawo))

for i in range(len(l)):
    if przekatn_lewno.count(l[i])>=2:
        for j in range(len(przekatn_lewno)):
            if l[i]==przekatn_lewno[j]:
                lew.append(j)

for i in range(len(p)):
    if przekatn_prawo.count(p[i])>=2:
        for j in range(len((przekatn_prawo))):
            if p[i]==przekatn_prawo[j]:
                praw.append(j)
print(lew)
print(praw)
wyn=lew+praw
koniec=[]
wyn=list(dict.fromkeys(wyn))
for i in wyn:
    print(dane[i])
    koniec.append(dane[i])
print(koniec)
pom=[]
o=0.5
while o<m:
    pom.append(o)
    o+=1
plt.xticks(pom)
plt.yticks(pom)
plt.scatter(x, y ,label= "gonce",color='blue' ,marker='o')
x1=[i[0] for i in koniec]
y1=[i[1] for i in koniec]
plt.scatter(x1, y1 ,label= "bijace", color='red' ,marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,10,0,10])
plt.legend()
plt.grid()
plt.show()


#  0 1 2 3 4 5 6
#0 0 1 2 3 4 5 6     +
#1 1 2 3 4 5 6 7
#2 2 3 4 5 6
#3 3 4 5 6 7
#4

#  0 1 2 3 4 5 6
#0 0 1 2 3 4 5 6     +
#1-1 0 1 2 3 4 5
#2-2-1 0 1 2
#3 3-2-1 0 1
#4
