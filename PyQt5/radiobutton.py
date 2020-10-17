import sys
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QRadioButton

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radyoyazisi=QLabel("Hangi Dili Daha Çok Seviyon?")
        self.java=QRadioButton("Java")
        self.python=QRadioButton("Python")
        self.php=QRadioButton("Php")

        self.yazialani=QLabel("")
        self.button=QPushButton("Gönder")

        v_box=QVBoxLayout()

        v_box.addWidget(self.radyoyazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.button)

        self.setLayout(v_box)
        self.button.clicked.connect(lambda : self.click(self.java.isChecked(),self.python.isChecked(),self.php.isChecked(),self.yazialani))
        self.setWindowTitle("Radio Button")
        self.show()
    def click(self,java,python,php,yazialani):
        if java:
            yazialani.setText("Java")
        if python:
            yazialani.setText("Python")
        if php:
            yazialani.setText("Php")


app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())