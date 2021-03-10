from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import json

import sys
with open("settings.json", "r+") as k:
    opo = json.loads(k.read())

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.setWindowTitle("OPENBULLET V2")
        self.setWindowIcon(QIcon('favicon.ico'))
        self.showMaximized()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(opo["Pannel_URL"]))

        self.setCentralWidget(self.browser)

        self.show()

app = QApplication(sys.argv)
window = MainWindow()

app.exec_()