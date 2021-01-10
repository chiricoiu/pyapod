import os
import requests
import json
import datetime, time
import random

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5 import QtGui


import apod_object_parser


class MainWin(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MainWin, self).__init__()
        self.img = QtGui.QImage()

        self.start_date = '1995-06-16'
        self.today_date = datetime.date.today()
        self.today_date_str = str(self.today_date)

        self.initUI()

        self.dateEdit.setMaximumDate(QtCore.QDate(self.today_date.year, self.today_date.month, self.today_date.day))
        self.dateEdit.setDate(QtCore.QDate(self.today_date.year, self.today_date.month, self.today_date.day))

        # controls
        self.random_Button.clicked.connect(self.change_random)

        
    def initUI(self):
        try:
            path = os.path.join(os.path.dirname(__file__), "form.ui")
            ui_file = uic.loadUi(path, self)
            self.load_data(self.today_date_str)
            self.show()
        except Exception as e:
            print(e)

    
    def showImg(self, img_url):
        try:
            self.img.loadFromData(requests.get(img_url).content)

            self.pixmap = QtGui.QPixmap(
                self.img.scaledToHeight(self.img_label.height()))
            self.img_label.setPixmap(self.pixmap)
        except Exception as e:
            print(e)


    def showcontent(self, title, date, explanation):
        try:
            self.title_label.setText(title)
            self.date_label.setText(date)
            self.explanation_QTextBrowser.setText(explanation)
        except Exception as e:
            print(e)


    def load_data(self, date):
        try:
            api_key = '4M5w5Q9nBUEvG66YPfj8H4dRJACj48nbdmGiEDV2'
            request = 'date=' + date
            response = apod_object_parser.get_data(api_key + '&' + request)

            media_type = apod_object_parser.get_media_type(response)
            date = apod_object_parser.get_date(response)
            title = apod_object_parser.get_title(response)
            explanation = apod_object_parser.get_explanation(response)

            self.showcontent(title, date, explanation)
            if media_type == 'image':
                hd_img = apod_object_parser.get_hdurl(response)
                self.showImg(hd_img)
        except Exception as e:
            print(e)

    
    def change_random(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        try:
            stime = time.mktime(time.strptime(self.start_date, "%Y-%m-%d"))
            etime = time.mktime(time.strptime(self.today_date_str, "%Y-%m-%d"))
            ptime = stime + random.random() * (etime - stime)
            self.load_data(time.strftime("%Y-%m-%d", time.localtime(ptime)))
        except Exception as e:
            print(e)
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()
        
    def update_date(self, date):
        try:
            self.dateEdit.setDate(date)
        except Exception as e:
            print(e)
