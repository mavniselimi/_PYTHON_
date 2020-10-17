import sys
import requests
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def cevirici(self,doviz1,doviz2,dovizMiktar):
        api_key="5602d650ec7fd2264838303218664d93"
        url = "http://data.fixer.io/api/latest?access_key=" + api_key
        limkk=requests.get(url)

        infos = limkk.json()


        firstValue = infos["rates"][doviz1]
        secondValue = infos["rates"][doviz2]

        return "Sonuç==>>>>>>"+str((secondValue / firstValue) * dovizMiktar)

    def init_ui(self):
        self.doviz1aciklama=QtWidgets.QLabel("Çevirecek Olduğun Döviz Miktarını Gir>>>")
        self.doviz1miktar=QtWidgets.QLineEdit()
        self.doviz1aciklama2=QtWidgets.QLabel("Çevirecek Olduğun Paranızın Döviz Miktarının Cinsini Gir>>>")
        self.dolar=QtWidgets.QRadioButton("Dolar")
        self.euro=QtWidgets.QRadioButton("Euro")
        self.tl=QtWidgets.QRadioButton("Türk Lirası")
        self.doviz2aciklama1=QtWidgets.QLabel("Çevirmeyi Planladığınız Para Birimini Seçiniz")
        self.dolar2=QtWidgets.QRadioButton("Dolar")
        self.euro2=QtWidgets.QRadioButton("Euro")
        self.tl2=QtWidgets.QRadioButton("Türk Lirası")
        self.buton=QtWidgets.QPushButton("İşlemlerin Bitti İse Bana Tıkla")
        self.sonuc=QtWidgets.QLabel("")
        self.btngroup1 = QtWidgets.QButtonGroup()
        self.btngroup2 = QtWidgets.QButtonGroup()
        self.btngroup1.addButton(self.dolar)
        self.btngroup1.addButton(self.euro)
        self.btngroup1.addButton(self.tl)
        self.btngroup2.addButton(self.dolar2)
        self.btngroup2.addButton(self.euro2)
        self.btngroup2.addButton(self.tl2)

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.doviz1aciklama)
        v_box.addWidget(self.doviz1miktar)
        v_box.addWidget(self.doviz1aciklama2)
        v_box.addWidget(self.dolar)
        v_box.addWidget(self.euro)
        v_box.addWidget(self.tl)
        v_box.addWidget(self.doviz2aciklama1)
        v_box.addWidget(self.dolar2)
        v_box.addWidget(self.euro2)
        v_box.addWidget(self.tl2)
        v_box.addStretch()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.sonuc)
        self.buton.clicked.connect(lambda : self.click(self.tl.isChecked(),self.euro.isChecked(),self.dolar.isChecked(),self.tl2.isChecked(),self.euro2.isChecked(),self.dolar2.isChecked(),self.sonuc))
        self.setLayout(v_box)
        self.setWindowTitle("Döviz Çevirici")
        self.show()
    def click(self,tl,euro,dolar,tl2,euro2,dolar2,sonuc):
        miktar=float(self.doviz1miktar.text())
        if tl:
            if tl2:
                sonuc.setText(self.cevirici("TRY","TRY",miktar))
            if euro2:
                sonuc.setText(self.cevirici("TRY","EUR",miktar))
            if dolar2:
                sonuc.setText(self.cevirici("TRY","USD",miktar))
        if euro:
            if tl2:
                sonuc.setText(self.cevirici("EUR","TRY",miktar))
            if euro2:
                sonuc.setText(self.cevirici("EUR","EUR",miktar))
            if dolar2:
                sonuc.setText(self.cevirici("EUR","USD",miktar))
        if dolar:
            if tl2:
                sonuc.setText(self.cevirici("USD","TRY",miktar))
            if euro2:
                sonuc.setText(self.cevirici("USD","EUR",miktar))
            if dolar2:
                sonuc.setText(self.cevirici("USD","USD",miktar))




app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())