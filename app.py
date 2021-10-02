from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

# creating basic class for main window
class MyWebBrowser(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)
        
        self.window = QWidget()
        self.window.setWindowTitle("My simple Web Browser 🌐")

        # starting to define ui elements
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        # creating url bar
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        # creating the go button
        self.go_btn = QPushButton("Go")
        self.go_btn.setMaximumHeight(30)

        # creating the back button
        self.back_btn = QPushButton("◁")
        self.back_btn.setMaximumHeight(30)
        
        # creating the forward  button
        self.forward_btn = QPushButton("▷")
        self.forward_btn.setMaximumHeight(30)

        # adding the above buttons to horizontal layout
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
