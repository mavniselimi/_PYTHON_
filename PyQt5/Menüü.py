import sys
import os
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QApplication, QAction, qApp, QMainWindow,QFileDialog,QTextEdit

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle= menubar.addMenu("Düzenle")
        self.yazialani=QTextEdit()
        dosya_ac = QAction("Dosya Aç", self)

        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet=QAction("Dosya Kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")
        cikis=QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Alt+F4")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)
        v_box=QVBoxLayout()
        v_box.addWidget(self.yazialani)
        v_box.addStretch()
        self.setLayout(v_box)

        ara_ve_degistir=duzenle.addMenu("Ara ve Değiştir")
        ara=QAction("Ara", self)
        temizle=QAction("Temizle",self)
        degistir=QAction("Değiştir", self)
        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)
        duzenle.addAction(temizle)
        cikis.triggered.connect(self.cikisyap)
        dosya.triggered.connect(self.dosyaIslemleri)
        self.setWindowTitle("Menüler")
        self.show()
    def cikisyap(self):
        qApp.quit()
    def dosyaIslemleri(self,action):
        if action.text()=="Dosya Aç":
            dosya_ismi=QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
            with open(dosya_ismi[0],"r") as file:
                self.yazialani.setText(file.read())
app=QApplication(sys.argv)
menu=Menu()
sys.exit(app.exec_())