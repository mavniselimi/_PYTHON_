p=0
po=0
for i in range(1,101):
    p+=i
    po+=pow(i,2)
print("İlk 100 doğal sayının kareleri toplamı ile toplamlarının kareleri arasındaki farkı====>",pow(p,2)-po)
