import sys
import requests
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

from win32api import GetSystemMetrics


class MainWin(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()


        self.img_label = QtWidgets.QLabel(self)        
        self.img = QtGui.QImage()      
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(0,0,GetSystemMetrics(0),GetSystemMetrics(1))
        self.setWindowTitle('Astronomy Picture of the Day')
        self.show()
    
    def showImg(self, img_url):
        self.img.loadFromData(requests.get(img_url).content)

        self.pixmap = QtGui.QPixmap(self.img.scaledToHeight(1440))
        self.img_label.setPixmap(self.pixmap)
        self.img_label.resize(self.width(), self.height())