czypierwsza = "tak"
n=input()
n=int(n)
l=int(n**(1/2))
for i in range(2,l+1):
    if n%i==0:
        #print(n,i)
        #print("ni")
        czypierwsza="nie"
        break
print(czypierwsza)
