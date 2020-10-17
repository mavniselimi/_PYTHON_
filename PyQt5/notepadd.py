import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QTextEdit,QRadioButton,QPushButton,QVBoxLayout,QHBoxLayout,QFileDialog

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazialani=QTextEdit()
        self.temizle=QPushButton("Temizle")
        self.ac=QPushButton("Aç")
        self.kaydet=QPushButton("Kaydet")
        h_box=QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box=QVBoxLayout()
        v_box.addWidget(self.yazialani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")
        self.temizle.clicked.connect(self.temizlee)
        self.ac.clicked.connect(self.dosyaac)
        self.kaydet.clicked.connect(self.dosyakaydet)
        self.show()

        pass
    def temizlee(self):
        self.yazialani.clear()
    def dosyaac(self):
        dosya_ismi=QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        with open(dosya_ismi[0],"r") as file:
            self.yazialani.setText(file.read())

    def dosyakaydet(self):
        dosya_ismi=QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazialani.toPlainText())









app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())