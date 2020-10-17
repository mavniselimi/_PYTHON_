import sys

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox=QCheckBox("Pythonu Seviyor Musunuz?")
        self.yazi_alani=QLabel("")
        self.buon=QPushButton("bana tıkla")

        v_box=QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buon)

        self.setLayout(v_box)

        self.setWindowTitle("Checkbox")

        self.buon.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))
        self.show()
    def click(self,checkbox,yazi_alani):
        if checkbox:
            yazi_alani.setText("Pythonu seviyorsun hll")
        else:
            yazi_alani.setText("Niye Sevmiyon Oç")


app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())