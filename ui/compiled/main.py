# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainNLFbdq.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 657)
        icon = QIcon()
        icon.addFile(u":/ui/MaterialSymbolsMonitorHeart.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionShow_Cores = QAction(MainWindow)
        self.actionShow_Cores.setObjectName(u"actionShow_Cores")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame_7)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.pb_cpu_freq = QProgressBar(self.frame_3)
        self.pb_cpu_freq.setObjectName(u"pb_cpu_freq")
        self.pb_cpu_freq.setValue(24)

        self.horizontalLayout_2.addWidget(self.pb_cpu_freq)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lbl_cpu_temp = QLabel(self.frame_4)
        self.lbl_cpu_temp.setObjectName(u"lbl_cpu_temp")

        self.horizontalLayout_3.addWidget(self.lbl_cpu_temp)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.lbl_mem_total = QLabel(self.groupBox_2)
        self.lbl_mem_total.setObjectName(u"lbl_mem_total")

        self.gridLayout.addWidget(self.lbl_mem_total, 0, 1, 1, 1)

        self.lbl_mem_used = QLabel(self.groupBox_2)
        self.lbl_mem_used.setObjectName(u"lbl_mem_used")

        self.gridLayout.addWidget(self.lbl_mem_used, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.lbl_mem_free = QLabel(self.groupBox_2)
        self.lbl_mem_free.setObjectName(u"lbl_mem_free")

        self.gridLayout.addWidget(self.lbl_mem_free, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.frame_7)
        self.groupBox_5.setObjectName(u"groupBox_5")

        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.frame_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.pb_gpu_freq = QProgressBar(self.frame_5)
        self.pb_gpu_freq.setObjectName(u"pb_gpu_freq")
        self.pb_gpu_freq.setValue(24)

        self.horizontalLayout_4.addWidget(self.pb_gpu_freq)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.groupBox_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_gpu_men_used = QLabel(self.frame_6)
        self.lbl_gpu_men_used.setObjectName(u"lbl_gpu_men_used")

        self.gridLayout_2.addWidget(self.lbl_gpu_men_used, 2, 1, 1, 1)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.lbl_gpu_men_total = QLabel(self.frame_6)
        self.lbl_gpu_men_total.setObjectName(u"lbl_gpu_men_total")

        self.gridLayout_2.addWidget(self.lbl_gpu_men_total, 1, 1, 1, 1)

        self.lbl_gpu_mem_free = QLabel(self.frame_6)
        self.lbl_gpu_mem_free.setObjectName(u"lbl_gpu_mem_free")

        self.gridLayout_2.addWidget(self.lbl_gpu_mem_free, 3, 1, 1, 1)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.pb_gpu_mem_percent = QProgressBar(self.frame_6)
        self.pb_gpu_mem_percent.setObjectName(u"pb_gpu_mem_percent")
        self.pb_gpu_mem_percent.setValue(24)

        self.gridLayout_2.addWidget(self.pb_gpu_mem_percent, 4, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.groupBox_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)

        self.lbl_gpu_temp = QLabel(self.frame_8)
        self.lbl_gpu_temp.setObjectName(u"lbl_gpu_temp")

        self.gridLayout_3.addWidget(self.lbl_gpu_temp, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.lbl_gpu_fan_speed = QLabel(self.frame_8)
        self.lbl_gpu_fan_speed.setObjectName(u"lbl_gpu_fan_speed")

        self.gridLayout_3.addWidget(self.lbl_gpu_fan_speed, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.verticalLayout.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(160, 270, 131, 17))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(150, 250, 141, 17))
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 793, 22))
        self.menuPreferencies = QMenu(self.menuBar)
        self.menuPreferencies.setObjectName(u"menuPreferencies")
        self.menuCPU = QMenu(self.menuPreferencies)
        self.menuCPU.setObjectName(u"menuCPU")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuPreferencies.menuAction())
        self.menuPreferencies.addAction(self.menuCPU.menuAction())
        self.menuCPU.addAction(self.actionShow_Cores)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Free monitor", None))
        self.actionShow_Cores.setText(QCoreApplication.translate("MainWindow", u"Show Cores", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Usage", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Temp.", None))
        self.lbl_cpu_temp.setText(QCoreApplication.translate("MainWindow", u"0C", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Mem", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.lbl_mem_total.setText(QCoreApplication.translate("MainWindow", u"0.0B", None))
        self.lbl_mem_used.setText(QCoreApplication.translate("MainWindow", u"0.0B", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Free", None))
        self.lbl_mem_free.setText(QCoreApplication.translate("MainWindow", u"0.0B", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Network", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Usage", None))
        self.lbl_gpu_men_used.setText(QCoreApplication.translate("MainWindow", u"0B", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.lbl_gpu_men_total.setText(QCoreApplication.translate("MainWindow", u"0B", None))
        self.lbl_gpu_mem_free.setText(QCoreApplication.translate("MainWindow", u"0B", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Free", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Memory", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Temp", None))
        self.lbl_gpu_temp.setText(QCoreApplication.translate("MainWindow", u"0c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fan speed", None))
        self.lbl_gpu_fan_speed.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Process monitor", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"core CPU detail", None))
        self.menuPreferencies.setTitle(QCoreApplication.translate("MainWindow", u"Preferencies", None))
        self.menuCPU.setTitle(QCoreApplication.translate("MainWindow", u"CPU", None))
    # retranslateUi

