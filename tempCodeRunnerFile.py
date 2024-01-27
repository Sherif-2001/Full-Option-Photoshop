from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QKeySequence,QShortcut
from PySide6.QtCore import Qt
from mainwindow import MainWindow

app = QApplication(sys.argv)
app.setStyle(QStyleFactory.create('Fusion'))

mainwindow = MainWindow()

esc_shortcut = QShortcut(QKeySequence(Qt.Key_Escape), mainwindow)
esc_shortcut.activated.connect(mainwindow.close)

mainwindow.showFullScreen()
mainwindow.show()

app.exec()