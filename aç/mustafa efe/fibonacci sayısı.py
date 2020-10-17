sayi = int(input("Ne kadar devam etsin"))
a = 1
b = 1
fibonacci = [a,b]
for i in range(sayi):
    a,b = b,a+b #b'yi a'ya attık, a+b'yi de b'ye attık
    fibonacci.append(b) #listeye ekliyoruz.
 
print(fibonacci)
