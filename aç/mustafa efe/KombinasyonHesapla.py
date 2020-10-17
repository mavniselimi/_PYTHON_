def fakto(i):
    
    if i==1:       
        return 1
    
    else: 
        return i * fakto(i-1)
    
def kom(ina,inan):
    return (fakto(ina)/(fakto(ina-inan)*fakto(inan)))
print("Kombinasyon hesabı için lütfen sayıları giriniz.")   
 
sayi1 = int(input("1. Sayı Giriniz: "))
 
sayi2 = int(input("2. Sayı Giriniz: ")) 
 
print("\nSonuç:",kom(sayi1,sayi2))
