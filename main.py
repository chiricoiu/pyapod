import sys
from PyQt5 import QtWidgets

from app import MainWin


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    apod = MainWin()
    apod.setWindowTitle('Astrology Picture of the Day')
    sys.exit(app.exec_())