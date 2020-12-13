import sys
import os
import requests

from PyQt5 import QtWidgets 
from PyQt5 import uic
from PyQt5 import QtGui


class MainWin(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainWin, self).__init__()
        self.img = QtGui.QImage()
        self.initUI()

        
    def initUI(self):
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = uic.loadUi(path, self)
        self.show()

    
    def showImg(self, img_url):
        self.img.loadFromData(requests.get(img_url).content)

        self.pixmap = QtGui.QPixmap(
            self.img.scaledToHeight(self.img_label.height()))
        self.img_label.setPixmap(self.pixmap)
        self.img_label.resize(1920, 1080)

    def showcontent(self, title, explaination):
        self.title_label.setText(title)
        self.explain_label.setText(explaination)