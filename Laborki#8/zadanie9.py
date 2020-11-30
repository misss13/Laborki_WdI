#Wszystko wypisze
tab=[]

def Suma(n):
    if sum(tab) == n:#war1
        #print(tab)
        print("%d + " %(tab[0]),end="")
        for i in range(1,len(tab)-1):
            print("%d + " %(tab[i]), end="")
        print("%d = %d " %(tab[len(tab)-1],n))
    if sum(tab) < n:#war2
        for i in range(1, n):
            tab.append(i)
            Suma(n)
            tab.pop()

if __name__ == '__main__':
    while 1:
        try:
            n=int(input("Prosze podac n: "))
            if n<0:
                print("Liczba musi być większa od zera")
                continue
            break
        except:
            print("To nie jest liczba calkowita")
            continue
    Suma(n)
