import requests
import json
import sys
import PyQt5.QtWidgets as Qt

from app import Example


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def request():
    api_key = '4M5w5Q9nBUEvG66YPfj8H4dRJACj48nbdmGiEDV2'
    url = 'https://api.nasa.gov/planetary/apod?'
    query = ''

    r1 = requests.get(url + 'api_key=' + api_key + query)
    jprint(r1.json())


if __name__ == "__main__":
    app = Qt.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 