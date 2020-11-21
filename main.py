import requests
import json
import sys
import datetime

import PyQt5.QtWidgets as Qt

from app import MainWin
import apod_object_parser


if __name__ == "__main__":
    response = apod_object_parser.get_data('4M5w5Q9nBUEvG66YPfj8H4dRJACj48nbdmGiEDV2&date=2013-01-09')
    url = apod_object_parser.get_hdurl(response)
    app = Qt.QApplication(sys.argv)
    ex = MainWin()
    ex.showImg(url)
    sys.exit(app.exec_()) 