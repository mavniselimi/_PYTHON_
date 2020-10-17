sayi = input("Sayi giriniz:")
kuvvet = len(sayi) #Basamak değerini aldık.
sayi = int(sayi)
toplam = 0
rakam = 0
kontrol = sayi
for i in range(kuvvet):
    rakam = sayi % 10 # Kalanı aldık.
    toplam += rakam ** kuvvet # Kuvvetini aldık.
    sayi = sayi // 10 # Bölümü aldık.
 
if(toplam == kontrol):
    print("Armstrong sayıdır")
else:
    print("Armstrong sayısı değildir")
