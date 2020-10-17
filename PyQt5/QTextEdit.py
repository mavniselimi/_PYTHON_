import sys

from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QTextEdit,QRadioButton,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.yazialani=QTextEdit()
        self.temizle=QPushButton("Temizle")

        v_box=QVBoxLayout()

        v_box.addWidget(self.yazialani)
        v_box.addWidget(self.temizle)

        self.setWindowTitle("Yazi Alani")

        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)
        self.show()

    def click(self):
        self.yazialani.clear()

app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())