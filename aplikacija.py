from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush


class Gui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()
        self.show()

    def initGui(self):
  #komentar


app = QtWidgets.QApplication([])
window = Gui()
app.exec_()
