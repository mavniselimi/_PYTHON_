for sayi in range(1,100000):
    kac_haneli=len(str(sayi))
    toplam=0
    for hane in range( kac_haneli):
        belirtilen_hane=str(sayi)[hane]
        c=1
        for b in range(int(belirtilen_hane)):
            c=c*(b+1)
        toplam+=c
    if toplam==sayi:
        print(sayi)
