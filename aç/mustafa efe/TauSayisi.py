f=int(input("Bir sayi gir:"))
a=0
for i in range(1,f+1):
    if (f%i==0):
        a+=1
if f%a==0:
    print(f,"Bir Tau Sayısıdır")
else:
    print(f,"Bir Tau Sayısı Değildir")
