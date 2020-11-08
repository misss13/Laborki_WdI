dzielniki=[1]
a=input()
a=int(a)
for i in range(2,a):
    if a%i==0:
        dzielniki.append(i)
dzielniki.append(a)
print("dzielniki:")
print(dzielniki)
