class Eror_mniejsza(Exception):
    pass

a=1 #poczatek przedzialu
while True:
    try:
        b=int(input("Prosze podac koniec przedzialu: ")) #koniec przedzialu
        break
    except:
        print("zla wartosc konca przedzialu ")
        continue
n=100 #liczba prostokatow na ktore dzielimy szukane pole
if a>=b:
    print("za maly przedzial")
    raise Eror_mniejsza
    quit()
x=(b-a)/n #szerokosc boku 1dnego prostokats
s=a+x/2 #srodek prostokata
P=0
#print(x) #debug
for i in range(0,n): #f(srodek w danym momencie prostokata) czyli sumujemy wysokosci az do (n-1)
    P+=(1/(s+(i*x)))
    #print(1/(s+(i*x))) #debug
P*=x #bo przek
print("Pole wynosi:")
print(P)
