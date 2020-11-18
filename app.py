import sys
import PyQt5.QtWidgets as Qt


class Example(Qt.QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Astronomy Picture of the Day')
    
        self.show()