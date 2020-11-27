#Zadanie 9. Proszę napisać program wskazujący (rekurencyjnie) wszystkie możliwe
# podziały liczby naturalnej na sumę składników. Na przykład dla liczby
#4 są to:1+3, 1+1+2, 1+1+1+1, 2+2.
#wypisuje tak jak w zadaniu
tab=[]

def Suma(n,k):
    if sum(tab) == n:
        #print(tab)
        print("%d + " %(tab[0]),end="")
        for i in range(1,len(tab)-1):
            print("%d + " %(tab[i]), end="")
        print("%d = %d " %(tab[len(tab)-1],n))
    if sum(tab) < n:
        for i in range(k, n):
            tab.append(i)
            Suma(n,k)
            k+=1
            tab.pop()

if __name__ == '__main__':
    while 1:
        try:
            n=int(input("Prosze podac n: "))
            break
        except:
            print("To nie jest liczba calkowita")
            continue
    Suma(n,1)
