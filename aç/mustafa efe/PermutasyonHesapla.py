def fakto(i):
    
    if i==1:       
        return 1
    
    else: 
        return i * fakto(i-1)
    
def per(ina,inan):
    return (fakto(ina)/(fakto(ina-inan)))
print("Permütasyon hesabı için lütfen sayıları giriniz.")   
 
sayi1 = int(input("1. Sayı Giriniz: "))
 
sayi2 = int(input("2. Sayı Giriniz: ")) 
 
print("\nSonuç:",per(sayi1,sayi2))
