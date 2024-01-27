# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 808)
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
        self.groupBox_6.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.saltandpepper_radio = QRadioButton(self.groupBox_6)
        self.saltandpepper_radio.setObjectName(u"saltandpepper_radio")
        self.saltandpepper_radio.setChecked(True)
        self.saltandpepper_radio.setAutoRepeat(False)
        self.saltandpepper_radio.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.saltandpepper_radio)

        self.gaussian_radio = QRadioButton(self.groupBox_6)
        self.gaussian_radio.setObjectName(u"gaussian_radio")
        self.gaussian_radio.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.gaussian_radio)

        self.uniform_radio = QRadioButton(self.groupBox_6)
        self.uniform_radio.setObjectName(u"uniform_radio")
        self.uniform_radio.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.uniform_radio)


        self.verticalLayout_16.addLayout(self.verticalLayout_17)


        self.verticalLayout_15.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.average_radio = QRadioButton(self.groupBox_7)
        self.average_radio.setObjectName(u"average_radio")
        self.average_radio.setChecked(True)

        self.verticalLayout_19.addWidget(self.average_radio)

        self.gaussianf_radio = QRadioButton(self.groupBox_7)
        self.gaussianf_radio.setObjectName(u"gaussianf_radio")

        self.verticalLayout_19.addWidget(self.gaussianf_radio)

        self.median_radio = QRadioButton(self.groupBox_7)
        self.median_radio.setObjectName(u"median_radio")

        self.verticalLayout_19.addWidget(self.median_radio)


        self.verticalLayout_18.addLayout(self.verticalLayout_19)


        self.verticalLayout_15.addWidget(self.groupBox_7)

        self.noise_btn = QPushButton(self.tab)
        self.noise_btn.setObjectName(u"noise_btn")

        self.verticalLayout_15.addWidget(self.noise_btn)

        self.groupBox_8 = QGroupBox(self.tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sobel_radio = QRadioButton(self.groupBox_8)
        self.sobel_radio.setObjectName(u"sobel_radio")
        self.sobel_radio.setChecked(True)

        self.gridLayout.addWidget(self.sobel_radio, 0, 0, 1, 1)

        self.roberts_radio = QRadioButton(self.groupBox_8)
        self.roberts_radio.setObjectName(u"roberts_radio")

        self.gridLayout.addWidget(self.roberts_radio, 1, 0, 1, 1)

        self.prewitt_radio = QRadioButton(self.groupBox_8)
        self.prewitt_radio.setObjectName(u"prewitt_radio")

        self.gridLayout.addWidget(self.prewitt_radio, 0, 1, 1, 1)

        self.canny_radio = QRadioButton(self.groupBox_8)
        self.canny_radio.setObjectName(u"canny_radio")

        self.gridLayout.addWidget(self.canny_radio, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.edge_btn = QPushButton(self.groupBox_8)
        self.edge_btn.setObjectName(u"edge_btn")

        self.verticalLayout_2.addWidget(self.edge_btn)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_15.addWidget(self.groupBox_8)

        self.groupBox_10 = QGroupBox(self.tab)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.line_radio = QRadioButton(self.groupBox_10)
        self.line_radio.setObjectName(u"line_radio")
        self.line_radio.setChecked(True)

        self.verticalLayout_26.addWidget(self.line_radio)

        self.circle_radio = QRadioButton(self.groupBox_10)
        self.circle_radio.setObjectName(u"circle_radio")

        self.verticalLayout_26.addWidget(self.circle_radio)

        self.ellipse_radio = QRadioButton(self.groupBox_10)
        self.ellipse_radio.setObjectName(u"ellipse_radio")

        self.verticalLayout_26.addWidget(self.ellipse_radio)

        self.hough_btn = QPushButton(self.groupBox_10)
        self.hough_btn.setObjectName(u"hough_btn")

        self.verticalLayout_26.addWidget(self.hough_btn)


        self.verticalLayout_25.addLayout(self.verticalLayout_26)


        self.verticalLayout_15.addWidget(self.groupBox_10)

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

        self.radius_spinbox = QSpinBox(self.groupBox_5)
        self.radius_spinbox.setObjectName(u"radius_spinbox")

        self.horizontalLayout_9.addWidget(self.radius_spinbox)


        self.verticalLayout_28.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.center_spinbox = QSpinBox(self.groupBox_5)
        self.center_spinbox.setObjectName(u"center_spinbox")

        self.horizontalLayout_10.addWidget(self.center_spinbox)


        self.verticalLayout_28.addLayout(self.horizontalLayout_10)

        self.contour_btn = QPushButton(self.groupBox_5)
        self.contour_btn.setObjectName(u"contour_btn")

        self.verticalLayout_28.addWidget(self.contour_btn)


        self.verticalLayout_33.addLayout(self.verticalLayout_28)


        self.verticalLayout_15.addWidget(self.groupBox_5)


        self.horizontalLayout.addLayout(self.verticalLayout_15)

        self.homeimage_lbl = QLabel(self.tab)
        self.homeimage_lbl.setObjectName(u"homeimage_lbl")
        self.homeimage_lbl.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.horizontalLayout.addWidget(self.homeimage_lbl)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.groupBox_9 = QGroupBox(self.tab)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.normalize_radio = QRadioButton(self.groupBox_9)
        self.normalize_radio.setObjectName(u"normalize_radio")
        self.normalize_radio.setChecked(True)

        self.verticalLayout_23.addWidget(self.normalize_radio)

        self.equalize_radio = QRadioButton(self.groupBox_9)
        self.equalize_radio.setObjectName(u"equalize_radio")

        self.verticalLayout_23.addWidget(self.equalize_radio)

        self.histogram_btn = QPushButton(self.groupBox_9)
        self.histogram_btn.setObjectName(u"histogram_btn")

        self.verticalLayout_23.addWidget(self.histogram_btn)

        self.rgbhist_btn = QPushButton(self.groupBox_9)
        self.rgbhist_btn.setObjectName(u"rgbhist_btn")

        self.verticalLayout_23.addWidget(self.rgbhist_btn)


        self.verticalLayout_22.addLayout(self.verticalLayout_23)


        self.verticalLayout_24.addWidget(self.groupBox_9)

        self.groupBox_11 = QGroupBox(self.tab)
        self.groupBox_11.setObjectName(u"groupBox_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy1)
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.harris_btn = QPushButton(self.groupBox_11)
        self.harris_btn.setObjectName(u"harris_btn")

        self.verticalLayout_27.addWidget(self.harris_btn)


        self.verticalLayout_24.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.tab)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.otsu_radio = QRadioButton(self.groupBox_12)
        self.otsu_radio.setObjectName(u"otsu_radio")
        self.otsu_radio.setChecked(True)

        self.verticalLayout_30.addWidget(self.otsu_radio)

        self.optimal_radio = QRadioButton(self.groupBox_12)
        self.optimal_radio.setObjectName(u"optimal_radio")

        self.verticalLayout_30.addWidget(self.optimal_radio)

        self.spectral_radio = QRadioButton(self.groupBox_12)
        self.spectral_radio.setObjectName(u"spectral_radio")

        self.verticalLayout_30.addWidget(self.spectral_radio)

        self.threshold_combobox = QComboBox(self.groupBox_12)
        self.threshold_combobox.addItem("")
        self.threshold_combobox.addItem("")
        self.threshold_combobox.setObjectName(u"threshold_combobox")

        self.verticalLayout_30.addWidget(self.threshold_combobox)

        self.threshold_btn = QPushButton(self.groupBox_12)
        self.threshold_btn.setObjectName(u"threshold_btn")

        self.verticalLayout_30.addWidget(self.threshold_btn)


        self.verticalLayout_29.addLayout(self.verticalLayout_30)


        self.verticalLayout_24.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.tab)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.kmeans_radio = QRadioButton(self.groupBox_13)
        self.kmeans_radio.setObjectName(u"kmeans_radio")
        self.kmeans_radio.setChecked(True)

        self.verticalLayout_14.addWidget(self.kmeans_radio)

        self.regiongrowing_radio = QRadioButton(self.groupBox_13)
        self.regiongrowing_radio.setObjectName(u"regiongrowing_radio")

        self.verticalLayout_14.addWidget(self.regiongrowing_radio)

        self.agglomerative_radio = QRadioButton(self.groupBox_13)
        self.agglomerative_radio.setObjectName(u"agglomerative_radio")

        self.verticalLayout_14.addWidget(self.agglomerative_radio)

        self.meanshift_radio = QRadioButton(self.groupBox_13)
        self.meanshift_radio.setObjectName(u"meanshift_radio")

        self.verticalLayout_14.addWidget(self.meanshift_radio)

        self.segment_btn = QPushButton(self.groupBox_13)
        self.segment_btn.setObjectName(u"segment_btn")

        self.verticalLayout_14.addWidget(self.segment_btn)


        self.verticalLayout_24.addWidget(self.groupBox_13)

        self.groupBox_14 = QGroupBox(self.tab)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.verticalLayout_40 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.homebrowse_btn = QPushButton(self.groupBox_14)
        self.homebrowse_btn.setObjectName(u"homebrowse_btn")

        self.verticalLayout_39.addWidget(self.homebrowse_btn)

        self.reset_btn = QPushButton(self.groupBox_14)
        self.reset_btn.setObjectName(u"reset_btn")

        self.verticalLayout_39.addWidget(self.reset_btn)


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
        self.hybridinputimage1_lbl = QLabel(self.tab_2)
        self.hybridinputimage1_lbl.setObjectName(u"hybridinputimage1_lbl")
        self.hybridinputimage1_lbl.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.verticalLayout_34.addWidget(self.hybridinputimage1_lbl)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hybridbrowse_btn = QPushButton(self.tab_2)
        self.hybridbrowse_btn.setObjectName(u"hybridbrowse_btn")

        self.horizontalLayout_3.addWidget(self.hybridbrowse_btn)

        self.miximages_btn = QPushButton(self.tab_2)
        self.miximages_btn.setObjectName(u"miximages_btn")

        self.horizontalLayout_3.addWidget(self.miximages_btn)


        self.verticalLayout_34.addLayout(self.horizontalLayout_3)

        self.hybridinputimage2_lbl = QLabel(self.tab_2)
        self.hybridinputimage2_lbl.setObjectName(u"hybridinputimage2_lbl")
        self.hybridinputimage2_lbl.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.verticalLayout_34.addWidget(self.hybridinputimage2_lbl)


        self.horizontalLayout_5.addLayout(self.verticalLayout_34)

        self.hybridoutputimage_lbl = QLabel(self.tab_2)
        self.hybridoutputimage_lbl.setObjectName(u"hybridoutputimage_lbl")
        self.hybridoutputimage_lbl.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.horizontalLayout_5.addWidget(self.hybridoutputimage_lbl)


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
        self.siftinputimage1_lbl = QLabel(self.tab_4)
        self.siftinputimage1_lbl.setObjectName(u"siftinputimage1_lbl")
        self.siftinputimage1_lbl.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.horizontalLayout_4.addWidget(self.siftinputimage1_lbl)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.siftbrowse_btn = QPushButton(self.tab_4)
        self.siftbrowse_btn.setObjectName(u"siftbrowse_btn")

        self.verticalLayout_13.addWidget(self.siftbrowse_btn)

        self.matchfeatures_btn = QPushButton(self.tab_4)
        self.matchfeatures_btn.setObjectName(u"matchfeatures_btn")

        self.verticalLayout_13.addWidget(self.matchfeatures_btn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)

        self.siftinputimage2_lbl = QLabel(self.tab_4)
        self.siftinputimage2_lbl.setObjectName(u"siftinputimage2_lbl")
        self.siftinputimage2_lbl.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.horizontalLayout_4.addWidget(self.siftinputimage2_lbl)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 2)

        self.verticalLayout_31.addLayout(self.horizontalLayout_4)

        self.siftoutputimage_lbl = QLabel(self.tab_4)
        self.siftoutputimage_lbl.setObjectName(u"siftoutputimage_lbl")
        self.siftoutputimage_lbl.setStyleSheet(u"background: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 10px")

        self.verticalLayout_31.addWidget(self.siftoutputimage_lbl)


        self.verticalLayout_32.addLayout(self.verticalLayout_31)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_12.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.saltandpepper_radio.setText(QCoreApplication.translate("MainWindow", u"Salt and Pepper", None))
        self.gaussian_radio.setText(QCoreApplication.translate("MainWindow", u"Gaussian", None))
        self.uniform_radio.setText(QCoreApplication.translate("MainWindow", u"Uniform", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Noise Filters", None))
        self.average_radio.setText(QCoreApplication.translate("MainWindow", u"Average", None))
        self.gaussianf_radio.setText(QCoreApplication.translate("MainWindow", u"Gaussian", None))
        self.median_radio.setText(QCoreApplication.translate("MainWindow", u"Median", None))
        self.noise_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Noise", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Edge Detection Filters", None))
        self.sobel_radio.setText(QCoreApplication.translate("MainWindow", u"Sobel", None))
        self.roberts_radio.setText(QCoreApplication.translate("MainWindow", u"Roberts", None))
        self.prewitt_radio.setText(QCoreApplication.translate("MainWindow", u"Prewitt", None))
        self.canny_radio.setText(QCoreApplication.translate("MainWindow", u"Canny", None))
        self.edge_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Edge Detection", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Hough Transform", None))
        self.line_radio.setText(QCoreApplication.translate("MainWindow", u"Line Detection", None))
        self.circle_radio.setText(QCoreApplication.translate("MainWindow", u"Circle Detection", None))
        self.ellipse_radio.setText(QCoreApplication.translate("MainWindow", u"Ellipse Detection", None))
        self.hough_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Hough Transform", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Active Contour", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Radius", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.contour_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Contour", None))
        self.homeimage_lbl.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.normalize_radio.setText(QCoreApplication.translate("MainWindow", u"Normalize", None))
        self.equalize_radio.setText(QCoreApplication.translate("MainWindow", u"Equalize", None))
        self.histogram_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.rgbhist_btn.setText(QCoreApplication.translate("MainWindow", u"Show RGB Histograms", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Harris Operator", None))
        self.harris_btn.setText(QCoreApplication.translate("MainWindow", u"Detect Corners", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Thresholding", None))
        self.otsu_radio.setText(QCoreApplication.translate("MainWindow", u"Otsu", None))
        self.optimal_radio.setText(QCoreApplication.translate("MainWindow", u"Optimal", None))
        self.spectral_radio.setText(QCoreApplication.translate("MainWindow", u"Spectral", None))
        self.threshold_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Global", None))
        self.threshold_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Local", None))

        self.threshold_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Thresholding", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.kmeans_radio.setText(QCoreApplication.translate("MainWindow", u"K-Means", None))
        self.regiongrowing_radio.setText(QCoreApplication.translate("MainWindow", u"Region Growing", None))
        self.agglomerative_radio.setText(QCoreApplication.translate("MainWindow", u"Agglomerative", None))
        self.meanshift_radio.setText(QCoreApplication.translate("MainWindow", u"Mean Shift", None))
        self.segment_btn.setText(QCoreApplication.translate("MainWindow", u"Apply Segmentation", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.homebrowse_btn.setText(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"Reset Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.hybridinputimage1_lbl.setText("")
        self.hybridbrowse_btn.setText(QCoreApplication.translate("MainWindow", u"Browse Images", None))
        self.miximages_btn.setText(QCoreApplication.translate("MainWindow", u"Mix Images", None))
        self.hybridinputimage2_lbl.setText("")
        self.hybridoutputimage_lbl.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Hybrid", None))
        self.siftinputimage1_lbl.setText("")
        self.siftbrowse_btn.setText(QCoreApplication.translate("MainWindow", u"Browse Images", None))
        self.matchfeatures_btn.setText(QCoreApplication.translate("MainWindow", u"Match Features", None))
        self.siftinputimage2_lbl.setText("")
        self.siftoutputimage_lbl.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"SIFT", None))
    # retranslateUi

