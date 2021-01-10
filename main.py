import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPalette, QColor

from app import MainWin

WHITE =     QColor(255, 255, 255)
BLACK =     QColor(0, 0, 0)
RED =       QColor(255, 0, 0)
PRIMARY =   QColor(53, 53, 53)
SECONDARY = QColor(35, 35, 35)
TERTIARY =  QColor(42, 130, 218)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    app.setStyle("Fusion")

    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window,          PRIMARY)
    dark_palette.setColor(QPalette.WindowText,      WHITE)
    dark_palette.setColor(QPalette.Base,            SECONDARY)
    dark_palette.setColor(QPalette.AlternateBase,   PRIMARY)
    dark_palette.setColor(QPalette.ToolTipBase,     WHITE)
    dark_palette.setColor(QPalette.ToolTipText,     WHITE)
    dark_palette.setColor(QPalette.Text,            WHITE)
    dark_palette.setColor(QPalette.Button,          PRIMARY)
    dark_palette.setColor(QPalette.ButtonText,      WHITE)
    dark_palette.setColor(QPalette.BrightText,      RED)
    dark_palette.setColor(QPalette.Link,            TERTIARY)
    dark_palette.setColor(QPalette.Highlight,       TERTIARY)
    dark_palette.setColor(QPalette.HighlightedText, BLACK)

    app.setPalette(dark_palette)

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    apod = MainWin()
    apod.setWindowTitle('Astrology Picture of the Day')
    sys.exit(app.exec_())