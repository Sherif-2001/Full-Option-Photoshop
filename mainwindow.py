from PySide6.QtWidgets import QMainWindow,QFileDialog
from PySide6.QtGui import QPixmap
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Computer Vision Project")

