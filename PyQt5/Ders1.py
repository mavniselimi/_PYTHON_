import sys

from PyQt5 import QtWidgets, QtGui


def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    okay=QtWidgets.QPushButton("Tamam")
    cancel=QtWidgets.QPushButton("İptal")
    h_box=QtWidgets.QHBoxLayout()
    h_box.addWidget(okay)
    h_box.addStretch()
    h_box.addWidget(cancel)
    pencere.setWindowTitle("PyQt5 Ders 1")
    buton1 = QtWidgets.QPushButton(pencere)
    buton1.setText("Burası Bir Butondur")
    etiket2=QtWidgets.QLabel(pencere)
    etiket2.setText("Merhaba Dünya")
    etiket2.move(400,30)
    buton1.move(500,30)
    etiket1 = QtWidgets.QLabel(pencere)
    pencere.setLayout(h_box)
    etiket1.setText("Burası Bir Yazıdır")
    etiket1_resim = QtWidgets.QLabel(pencere)
    etiket1_resim.setPixmap(QtGui.QPixmap("python.png"))
    etiket1_resim.move(75, 50)
    etiket1.move(200, 30)
    pencere.setGeometry(100, 100, 500, 500)
    pencere.show()
    sys.exit(app.exec_())


Pencere()
