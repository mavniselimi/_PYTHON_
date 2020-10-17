def us(a,b):
    i=1
    for h in range(1,b+1):
        i=i*a
    return i
il=int(input("Tabani gir===>"))
il2=int(input("Üssü gir===>"))
print(il," üssü ",il2," eşittir====>",us(il,il2))
