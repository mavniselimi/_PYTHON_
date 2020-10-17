def asalMi(sayi):
    sonuc=True
    for i in range(2,sayi):
        if(sayi%i == 0):
            sonuc=False
    return sonuc
 
 
sayi = int(input("Sayi:"))
if asalMi(sayi):
    print("Asal Sayıdır")
else:
    print("Asal Değildir")
