import requests
import json
import sys
import datetime

from PyQt5 import QtWidgets

import apod_object_parser
from app import MainWin


if __name__ == "__main__":
    api_key = '4M5w5Q9nBUEvG66YPfj8H4dRJACj48nbdmGiEDV2'
    request = 'date=2013-01-09'
    response = apod_object_parser.get_data(api_key + '&' + request)
    hd_img = apod_object_parser.get_hdurl(response)

    title = apod_object_parser.get_title(response)
    explain = apod_object_parser.get_explaination(response)

    app = QtWidgets.QApplication([])
    apod = MainWin()
    apod.showImg(hd_img)
    apod.showcontent(title, explain)
    sys.exit(app.exec_())