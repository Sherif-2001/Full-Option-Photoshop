from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        self.setWindowTitle("Computer Vision Project")
