from PySide6.QtWidgets import QApplication
import sys
from mainwindow import MainWindow

mainwindow = MainWindow()
app = QApplication(sys.argv)
app.exec()