# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 725)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.radioButton_17 = QRadioButton(self.groupBox_6)
        self.radioButton_17.setObjectName(u"radioButton_17")

        self.verticalLayout_17.addWidget(self.radioButton_17)

        self.radioButton_18 = QRadioButton(self.groupBox_6)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.verticalLayout_17.addWidget(self.radioButton_18)

        self.radioButton_19 = QRadioButton(self.groupBox_6)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.verticalLayout_17.addWidget(self.radioButton_19)


        self.verticalLayout_16.addLayout(self.verticalLayout_17)


        self.verticalLayout_15.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.radioButton_20 = QRadioButton(self.groupBox_7)
        self.radioButton_20.setObjectName(u"radioButton_20")

        self.verticalLayout_19.addWidget(self.radioButton_20)

        self.radioButton_21 = QRadioButton(self.groupBox_7)
        self.radioButton_21.setObjectName(u"radioButton_21")

        self.verticalLayout_19.addWidget(self.radioButton_21)

        self.radioButton_22 = QRadioButton(self.groupBox_7)
        self.radioButton_22.setObjectName(u"radioButton_22")

        self.verticalLayout_19.addWidget(self.radioButton_22)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)


        self.verticalLayout_15.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.radioButton_23 = QRadioButton(self.groupBox_8)
        self.radioButton_23.setObjectName(u"radioButton_23")

        self.verticalLayout_21.addWidget(self.radioButton_23)

        self.radioButton_24 = QRadioButton(self.groupBox_8)
        self.radioButton_24.setObjectName(u"radioButton_24")

        self.verticalLayout_21.addWidget(self.radioButton_24)

        self.radioButton_25 = QRadioButton(self.groupBox_8)
        self.radioButton_25.setObjectName(u"radioButton_25")

        self.verticalLayout_21.addWidget(self.radioButton_25)

        self.radioButton_26 = QRadioButton(self.groupBox_8)
        self.radioButton_26.setObjectName(u"radioButton_26")

        self.verticalLayout_21.addWidget(self.radioButton_26)


        self.verticalLayout_20.addLayout(self.verticalLayout_21)


        self.verticalLayout_15.addWidget(self.groupBox_8)

        self.groupBox_10 = QGroupBox(self.tab)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.radioButton_29 = QRadioButton(self.groupBox_10)
        self.radioButton_29.setObjectName(u"radioButton_29")

        self.verticalLayout_26.addWidget(self.radioButton_29)

        self.radioButton_30 = QRadioButton(self.groupBox_10)
        self.radioButton_30.setObjectName(u"radioButton_30")

        self.verticalLayout_26.addWidget(self.radioButton_30)

        self.radioButton_31 = QRadioButton(self.groupBox_10)
        self.radioButton_31.setObjectName(u"radioButton_31")

        self.verticalLayout_26.addWidget(self.radioButton_31)


        self.verticalLayout_25.addLayout(self.verticalLayout_26)


        self.verticalLayout_15.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.tab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.radioButton_27 = QRadioButton(self.groupBox_9)
        self.radioButton_27.setObjectName(u"radioButton_27")

        self.verticalLayout_23.addWidget(self.radioButton_27)

        self.radioButton_28 = QRadioButton(self.groupBox_9)
        self.radioButton_28.setObjectName(u"radioButton_28")

        self.verticalLayout_23.addWidget(self.radioButton_28)

        self.pushButton_2 = QPushButton(self.groupBox_9)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_23.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_9)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_23.addWidget(self.pushButton_3)


        self.verticalLayout_22.addLayout(self.verticalLayout_23)


        self.verticalLayout_15.addWidget(self.groupBox_9)


        self.horizontalLayout.addLayout(self.verticalLayout_15)

        self.mainImageLabel = QLabel(self.tab)
        self.mainImageLabel.setObjectName(u"mainImageLabel")
        self.mainImageLabel.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.horizontalLayout.addWidget(self.mainImageLabel)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_33 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.spinBox_5 = QSpinBox(self.groupBox_5)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.horizontalLayout_9.addWidget(self.spinBox_5)


        self.verticalLayout_28.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.spinBox_6 = QSpinBox(self.groupBox_5)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.horizontalLayout_10.addWidget(self.spinBox_6)


        self.verticalLayout_28.addLayout(self.horizontalLayout_10)

        self.pushButton_13 = QPushButton(self.groupBox_5)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_28.addWidget(self.pushButton_13)


        self.verticalLayout_33.addLayout(self.verticalLayout_28)


        self.verticalLayout_24.addWidget(self.groupBox_5)

        self.groupBox_11 = QGroupBox(self.tab)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy1)
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.pushButton_6 = QPushButton(self.groupBox_11)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_27.addWidget(self.pushButton_6)


        self.verticalLayout_24.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.tab)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.radioButton_35 = QRadioButton(self.groupBox_12)
        self.radioButton_35.setObjectName(u"radioButton_35")

        self.verticalLayout_30.addWidget(self.radioButton_35)

        self.radioButton_15 = QRadioButton(self.groupBox_12)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.verticalLayout_30.addWidget(self.radioButton_15)

        self.radioButton_36 = QRadioButton(self.groupBox_12)
        self.radioButton_36.setObjectName(u"radioButton_36")

        self.verticalLayout_30.addWidget(self.radioButton_36)

        self.comboBox = QComboBox(self.groupBox_12)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_30.addWidget(self.comboBox)


        self.verticalLayout_29.addLayout(self.verticalLayout_30)


        self.verticalLayout_24.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.tab)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.radioButton_32 = QRadioButton(self.groupBox_13)
        self.radioButton_32.setObjectName(u"radioButton_32")

        self.verticalLayout_14.addWidget(self.radioButton_32)

        self.radioButton_33 = QRadioButton(self.groupBox_13)
        self.radioButton_33.setObjectName(u"radioButton_33")

        self.verticalLayout_14.addWidget(self.radioButton_33)

        self.radioButton_34 = QRadioButton(self.groupBox_13)
        self.radioButton_34.setObjectName(u"radioButton_34")

        self.verticalLayout_14.addWidget(self.radioButton_34)

        self.radioButton_16 = QRadioButton(self.groupBox_13)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.verticalLayout_14.addWidget(self.radioButton_16)


        self.verticalLayout_24.addWidget(self.groupBox_13)

        self.groupBox_14 = QGroupBox(self.tab)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_40 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.pushButton_14 = QPushButton(self.groupBox_14)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_39.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.groupBox_14)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_39.addWidget(self.pushButton_15)


        self.verticalLayout_40.addLayout(self.verticalLayout_39)


        self.verticalLayout_24.addWidget(self.groupBox_14)


        self.horizontalLayout.addLayout(self.verticalLayout_24)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_35 = QVBoxLayout(self.tab_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.mainImageLabel_2 = QLabel(self.tab_2)
        self.mainImageLabel_2.setObjectName(u"mainImageLabel_2")
        self.mainImageLabel_2.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.verticalLayout_34.addWidget(self.mainImageLabel_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_3.addWidget(self.pushButton_8)


        self.verticalLayout_34.addLayout(self.horizontalLayout_3)

        self.mainImageLabel_3 = QLabel(self.tab_2)
        self.mainImageLabel_3.setObjectName(u"mainImageLabel_3")
        self.mainImageLabel_3.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.verticalLayout_34.addWidget(self.mainImageLabel_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_34)

        self.mainImageLabel_4 = QLabel(self.tab_2)
        self.mainImageLabel_4.setObjectName(u"mainImageLabel_4")
        self.mainImageLabel_4.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.horizontalLayout_5.addWidget(self.mainImageLabel_4)


        self.verticalLayout_35.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_32 = QVBoxLayout(self.tab_4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.mainImageLabel_6 = QLabel(self.tab_4)
        self.mainImageLabel_6.setObjectName(u"mainImageLabel_6")
        self.mainImageLabel_6.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.horizontalLayout_4.addWidget(self.mainImageLabel_6)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_11 = QPushButton(self.tab_4)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_13.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.tab_4)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_13.addWidget(self.pushButton_12)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)

        self.mainImageLabel_8 = QLabel(self.tab_4)
        self.mainImageLabel_8.setObjectName(u"mainImageLabel_8")
        self.mainImageLabel_8.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.horizontalLayout_4.addWidget(self.mainImageLabel_8)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 2)

        self.verticalLayout_31.addLayout(self.horizontalLayout_4)

        self.mainImageLabel_7 = QLabel(self.tab_4)
        self.mainImageLabel_7.setObjectName(u"mainImageLabel_7")
        self.mainImageLabel_7.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.verticalLayout_31.addWidget(self.mainImageLabel_7)


        self.verticalLayout_32.addLayout(self.verticalLayout_31)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_38 = QVBoxLayout(self.tab_3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(22)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.mainImageLabel_10 = QLabel(self.tab_3)
        self.mainImageLabel_10.setObjectName(u"mainImageLabel_10")
        self.mainImageLabel_10.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.verticalLayout_37.addWidget(self.mainImageLabel_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_9 = QPushButton(self.tab_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_11.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.tab_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_11.addWidget(self.pushButton_10)


        self.verticalLayout_37.addLayout(self.horizontalLayout_11)


        self.verticalLayout_41.addLayout(self.verticalLayout_37)

        self.line = QFrame(self.tab_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_41.addWidget(self.line)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.mainImageLabel_9 = QLabel(self.tab_3)
        self.mainImageLabel_9.setObjectName(u"mainImageLabel_9")
        self.mainImageLabel_9.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.verticalLayout_36.addWidget(self.mainImageLabel_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.tab_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout_36.addLayout(self.horizontalLayout_6)


        self.verticalLayout_41.addLayout(self.verticalLayout_36)


        self.verticalLayout_38.addLayout(self.verticalLayout_41)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_12.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"Salt and Pepper", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"Gaussian", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"Uniform", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Noise Filters", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"Average", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"Gaussian", None))
        self.radioButton_22.setText(QCoreApplication.translate("MainWindow", u"Median", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Edge Detection Filters", None))
        self.radioButton_23.setText(QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.radioButton_24.setText(QCoreApplication.translate("MainWindow", u"Roberts", None))
        self.radioButton_25.setText(QCoreApplication.translate("MainWindow", u"Prewitt", None))
        self.radioButton_26.setText(QCoreApplication.translate("MainWindow", u"Canny", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Hough Transform", None))
        self.radioButton_29.setText(QCoreApplication.translate("MainWindow", u"Line Detection", None))
        self.radioButton_30.setText(QCoreApplication.translate("MainWindow", u"Circle Detection", None))
        self.radioButton_31.setText(QCoreApplication.translate("MainWindow", u"Ellipse Detection", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.radioButton_27.setText(QCoreApplication.translate("MainWindow", u"Normalize", None))
        self.radioButton_28.setText(QCoreApplication.translate("MainWindow", u"Equalize", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Show Histograms", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Show RGB Histograms", None))
        self.mainImageLabel.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Active Contour", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Radius", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Apply Contour", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Harris Operator", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Detect Corners", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Thresholding", None))
        self.radioButton_35.setText(QCoreApplication.translate("MainWindow", u"Otsu", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"Optimal", None))
        self.radioButton_36.setText(QCoreApplication.translate("MainWindow", u"Spectral", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Global", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Local", None))

        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.radioButton_32.setText(QCoreApplication.translate("MainWindow", u"K-Means", None))
        self.radioButton_33.setText(QCoreApplication.translate("MainWindow", u"Region Growing", None))
        self.radioButton_34.setText(QCoreApplication.translate("MainWindow", u"Agglomerative", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"Mean Shift", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Clear all", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.mainImageLabel_2.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Browse Images", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Mix Images", None))
        self.mainImageLabel_3.setText("")
        self.mainImageLabel_4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Hybrid Image", None))
        self.mainImageLabel_6.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Browse Images", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Match Features", None))
        self.mainImageLabel_8.setText("")
        self.mainImageLabel_7.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"SIFT", None))
        self.mainImageLabel_10.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Draw ROC Curve", None))
        self.mainImageLabel_9.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Start Cam", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Stop Cam", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Face Detection", None))
    # retranslateUi

