import sys

from PyQt5 import QtWidgets, QtGui


def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    okay=QtWidgets.QPushButton("Tamam")
    cancel=QtWidgets.QPushButton("İptal")
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(okay)
    v_box.addWidget(cancel)
    v_box.addStretch()
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addLayout(v_box)
    pencere.setWindowTitle("PyQt5")
    pencere.setLayout(h_box)
    pencere.setGeometry(100, 100, 500, 500)
    pencere.show()
    sys.exit(app.exec_())

Pencere()