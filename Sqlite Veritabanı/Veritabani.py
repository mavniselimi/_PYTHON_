import sqlite3

baglanti= sqlite3.connect("kütüphane.db")

imlec=baglanti.cursor()
def tablo_olustur():
    imlec.execute("CREATE TABLE IF NOT EXISTS kitaplık(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_Sayısı INT)")
    baglanti.commit()
def veri_ekle():
    imlec.execute("Insert into kitaplık VALUES('İstanbul hatirası','Ahmet Ümit','Everest Yayınları',561)")
    baglanti.commit()
def veri_ekleUSER(isim,yazar,yayınevi,sayfa_sayısı):
    imlec.execute("Insert into kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    baglanti.commit()
def verileri_al():
    imlec.execute("Select * From kitaplık")
    liste=imlec.fetchall()
    print(liste)
def kitapadial():
    imlec.execute("Select İsim From kitaplık")
    liste2=imlec.fetchall()
    for i in liste2:
        print(i)
def verileri_al3(yayınevii):
    imlec.execute("Select * From kitaplık where Yayınevi = ?",(yayınevii,))
    data = imlec.fetchall()
    if data=="":
        print("Girdiğiniz Yayınevi Adı DAha Önce Kullanılmamıştır")
    else:
        for i in data:
            print(i)
def verileri_guncelleKITAP(eski_kitap,yeni_kitap):
    imlec.execute("Update kitaplık set İsim=? where İsim=?",(yeni_kitap,eski_kitap))
    baglanti.commit()
def verileri_sil(yazar):
    imlec.execute("Delete From kitaplık where Yazar=?",(yazar,))
    baglanti.commit()


tablo_olustur() 
isim=input("Kitap Adı:")
yazar=input("Yazar Adı:")
yayınevi=input("Yayınevi:")
sayfa_sayısı=int(input("Sayfa Sayısı:"))
veri_ekleUSER(isim,yazar,yayınevi,sayfa_sayısı)
verileri_al()
kitapadial()
verileri_sil("0")
yayınevii=input("Yayın Evi Adı Girin")
verileri_al3(yayınevii)
eski_kitap=input("Değiştirmek İstediğiniz Kitap Adını Giriniz(Yoksa Sıfır Giriniz):")
yeni_kitap=input("Değiştirmek İstediğiniz Kitabın Yeni Adını Giriniz(Yoksa Sıfır Giriniz):")
verileri_al()
kitapadial()
verileri_guncelleKITAP(eski_kitap,yeni_kitap)
baglanti.close()
