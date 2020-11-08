def czydoskonala(a):
    dzielniki=[1]
    for i in range(2,a):
        if a%i==0:
            dzielniki.append(i)
    if a == (sum(dzielniki)):
        return True
    else:
        return False
n=input()
n=int(n)
lista=[1]
for i in range (2,n):
    if czydoskonala(i):
        lista.append(i)
print("liczb doskonalych wśród n pierwszych")
print(lista)
