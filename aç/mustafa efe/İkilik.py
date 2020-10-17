l=int(input("Bir sayi gir"))
a=[]
while (l>0):
    a.append(l%2)
    l=l//2
a.reverse()
print("İkilik sonuc==>",a)
