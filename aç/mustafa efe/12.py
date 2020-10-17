x=int(input("Tabani giriniz:"))
y=int(input("Üssü giriniz:"))
o=pow(x,y)
ld=0
l=len(str(o))
for i in range(l):
    d=str(o)[i]
    ld+=int(d)
print("Girdiğiniz Uslu sayı",o,"olup rakamları toplamı==>",ld)
