p=0
def asalMi(i):
    p=0
    for a in range(2,i):
        if (i%a==0):
            p+=1
    if p!=0:
        return 0
    if p==0:
        return i
toplam=0
po=0
sayac=1
for ass in range(1,1001):
    po=asalMi(ass)
    if (po!=0):
        print(sayac,".asal sayı===",po)
        toplam+=po
        sayac+=1
print("1000 ile 1 arasında",sayac," kadar asal sayı vardır toplamları :",toplam)
        
        
