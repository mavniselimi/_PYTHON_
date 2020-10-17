def asalMi(sayi):
    sonuc=True
    for i in range(2,sayi):
        if(sayi%i == 0):
            sonuc=False
    return sonuc
l=[]
k=int(input("Sayiyi Gir"))
for p in range(2,k+1):
    if k%p==0 and ((asalMi(p))==1):
        l.append(p)
print(k,"Girdiğiniz Sayinin Asal Sayilara Ayrılmış Hali",l)
