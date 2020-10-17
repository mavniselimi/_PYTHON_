# tts_espeak01.py

import os
while True:
    OkunacakMetin=input("Metin Giriniz===>")
    y=""
    for a in OkunacakMetin.split():
        y+=a
    cad="espeak -s170 -vtr+m3 "+str(y)
    os.system(cad)
