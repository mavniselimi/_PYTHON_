def asalMi(sayi):
    sonuc=True
    for i in range(2,sayi):
        if(sayi%i == 0):
            sonuc=False
    return sonuc
b=0
for i in range(1,100000):
    if asalMi(i):
        b+=1
    if(b==1923):
        print("1923.asal sayi:::",i)
        break
