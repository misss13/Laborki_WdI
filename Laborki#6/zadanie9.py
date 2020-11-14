#Wykorzystując funkcje, proszę napisać program, który pobiera przykładowy tekst zapisany w pliku:

#Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nibh augue, suscipit a, scelerisque
#sed, lacinia in, mi. Cras vel lorem. Etiam pellentesque aliquet tellus. Phasellus pharetra nulla ac
#diam. Quisque semper justo at risus. Donec venenatis, turpis vel hendrerit interdum, dui ligula ultricies
#purus, sed posuere libero dui id orci. Nam congue, pede vitae dapibus aliquet, elit magna vulputate arcu,
#vel tempus metus leo non est. Etiam sit amet lectus quis est congue mollis. Phasellus congue lacus eget neque.
#Phasellus ornare, ante vitae consectetuer consequat, purus sapien ultricies dolor, et mollis pede metus eget nisi.
#Praesent sodales velit quis augue. Cras suscipit, urna at aliquam rhoncus, urna quam viverra nisi, in interdum massa
#nibh nec erat. A następnie zwraca wartość określającą liczbę zdań w danym tekście.

#Można w tym celu skorzystać z wyrażeń regularnych.
def zliczacz(a):#sposób 1
    b=0
    l=len(a)
    for czar in range(l):
        if (a[czar] == '.') and (czar!=l-1):
            if ((a[czar-1] in "abcdefghijklmnoprstowxyzq,;/\n ") or (a[czar+1] in "abcdefghijklmnoprstowxyzq,;/\n")):
                b+=1
        if ((a[czar] == '.') and (czar==l-1)):
                b+=1
    print(a[l-2])
    return b

path='/home/zuza/Dokumenty/Laborki_WdI/Laborki#6/t1'
tekst_file=open(path,'r')
tekst=tekst_file.read()

print(tekst)
c_1=zliczacz(tekst)
c_2=tekst.count('.')#sposob 2

if c_2== 0:
    print("brak zdan w danym tekscie")
else:
    print("liczba zdan w tekscie to: ")
    print("Sposobem 1 to %d" %(c_1) )
    print("Sposobem 2 to %d" %(c_2) )

tekst_file.close()
