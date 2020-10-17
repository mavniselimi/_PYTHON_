import sys
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import time
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QRadioButton

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radyoyazisi=QLabel("Hangi Sagopa Kajmer Şarkısını Daha Çok Seviyon?")
        self.java=QRadioButton("Avutsun Bahaneler")
        self.python=QRadioButton("Gölge Haramileri")
        self.php=QRadioButton("Ahmak Islatan")

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
            tts_vlc("ab.mp3")
            yazialani.setText("Avutsun Bahaneler")
        if python:
            tts_vlc("gh.mp3")
            yazialani.setText("Gölge Haramileri")
        if php:
            tts_vlc("ai.mp3")
            yazialani.setText("Ahmak Islatan")

def tts_vlc(filename):
    p = vlc.MediaPlayer(filename)
    p.play()
    time.sleep(1)

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())