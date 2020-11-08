a=0
b=1
n=input()
n=int(n)
c=0
for c in range(n-1): #bo 2 pierwsze elementy to 0 i 1 a range wykonuje sie do przedostatniego el.
    if c%2==0:
        a=a+b
        f=a
    else:
        b=b+a
        f=b
print(f)
