def tamBolen(sayi):
    tamBolenler=[]
    for i in range(1,sayi+1):
        if sayi % i == 0: #mod'unu aldık.
            tamBolenler.append(i) #listeye ekledik.
    return tamBolenler
 
 
sayi = int(input("Sayı:"))
print("Tam Bölenler:",tamBolen(sayi))
