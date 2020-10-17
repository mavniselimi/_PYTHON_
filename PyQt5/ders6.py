import sys
from PyQt5 import QtWidgets

class Arayuz(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.init__ui()

    def init__ui(self):
        self.yaziAlani=QtWidgets.QLineEdit()
        self.temizle=QtWidgets.QPushButton("Temizle")
        self.yazır= QtWidgets.QPushButton("Yazdır")

        v_box=QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yaziAlani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazır)
        v_box.addStretch()

        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)
        self.yazır.clicked.connect(self.click)

        self.show()

    def click(self):
        sender=self.sender()

        if sender.text() == "Temizle":
            self.yaziAlani.clear()
        else:
            print(self.yaziAlani.text())
app=QtWidgets.QApplication(sys.argv)
arayuz=Arayuz()
sys.exit(app.exec_())