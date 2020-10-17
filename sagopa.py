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
        self.button2=QPushButton("Durdur")

        v_box=QVBoxLayout()

        v_box.addWidget(self.radyoyazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.button)
        v_box.addWidget(self.button2)

        self.setLayout(v_box)
        self.sayac=0
        self.button.clicked.connect(lambda : self.click(self.java.isChecked(),self.python.isChecked(),self.php.isChecked(),self.yazialani,self.sayac,self.button2.isChecked()))
        self.setWindowTitle("Radio Button")
        self.show()
    def click(self,java,python,php,yazialani,sayac,sd):
        ab=sayac
        sik1=False
        sik2=False
        sik3=False
        if java and ab==sayac:
            sayac+=1
            p = vlc.MediaPlayer("ab.mp3")
            p.play()
            b = vlc.MediaPlayer("ai.mp3")
            b.pause()
            a = vlc.MediaPlayer("gh.mp3")
            a.pause()
            time.sleep(1)
            yazialani.setText("Avutsun Bahaneler")
            sik1=True
            if sd or sik2==True or sik3==True:
                p.pause()
        if python and ab==sayac:
            sayac+=1
            p = vlc.MediaPlayer("gh.mp3")
            p.play()
            time.sleep(1)
            yazialani.setText("Gölge Haramileri")
            sik2=True
            if sik1==True or sik3==True:
                p.pause()
        if php and ab==sayac:
            sayac+=1
            p = vlc.MediaPlayer("ai.mp3")
            p.play()
            time.sleep(1)
            yazialani.setText("Ahmak Islatan")
            sik3=True
            if sik2==True or sik1==True:
                p.pause()

def tts_vlc(filename):
    p = vlc.MediaPlayer(filename)
    p.play()
    time.sleep(1)

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
