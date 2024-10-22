# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asss.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from images.img import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 537)
        MainWindow.setMinimumSize(QSize(640, 537))
        MainWindow.setMaximumSize(QSize(640, 537))
        MainWindow.setStyleSheet(u"background-color: rgb(29, 34, 40);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QSize(400, 0))
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"border-radius: 15px;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"border-radius: 15px;")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.label_4)


        self.horizontalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"border-radius: 15px;")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.label_5)


        self.horizontalLayout_5.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setStyleSheet(u"background-image:url(:/newPrefix/png-clipart-coins-coins-thumbnail (1) 1.png);\n"
"background-repeat:none;\n"
"")
        self.label_2.setPixmap(QPixmap(u"../Downloads/money_img.png"))
        self.label_2.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 50))
        font = QFont()
        # font.setFamilies([u".Arial Hebrew Desk Interface"])
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #fff;")
        self.label.setTextFormat(Qt.PlainText)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setStyleSheet(u"background: none;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(250, 0))
        self.progressBar.setMaximumSize(QSize(250, 16777215))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius: 8px;\n"
"	background-color: rgb(42, 47, 53);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	\n"
"	background-color: rgb(10, 85, 255);\n"
"	border-radius: 8px;\n"
"}")
        self.progressBar.setValue(40)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 400))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 150))
        self.pushButton.setMaximumSize(QSize(150, 150))
        self.pushButton.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/fT6nvb2zUEk 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(150, 150))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setMaximumSize(QSize(16777215, 80))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.pushButton_5 = QPushButton(self.frame_14)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(140, 40))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 80))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.pushButton_4 = QPushButton(self.frame_13)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(140, 40))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_8.addWidget(self.pushButton_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 80))
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)

        self.pushButton_8 = QPushButton(self.frame_17)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(130, 30))
        self.pushButton_8.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_12.addWidget(self.pushButton_8)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_16)


        self.verticalLayout_2.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 80))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)

        self.pushButton_7 = QPushButton(self.frame_16)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(130, 30))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_11.addWidget(self.pushButton_7)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 80))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.pushButton_6 = QPushButton(self.frame_15)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(130, 30))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_10.addWidget(self.pushButton_6)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = QPushButton(self.frame_12)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(140, 40))
        self.pushButton_2.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamilies([u"a_Concepto"])
        font1.setPointSize(12)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 80))
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_17)

        self.pushButton_9 = QPushButton(self.frame_18)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(130, 30))
        self.pushButton_9.setStyleSheet(u"background-color: rgb(43, 48, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")

        self.horizontalLayout_13.addWidget(self.pushButton_9)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)


        self.verticalLayout_2.addWidget(self.frame_18)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c \u0437\u0430\n"
"        \u0442\u0430\u043f\n"
"         +9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043d\u0435\u0442 \u0434\u043b\u044f \n"
"      \u0430\u043f\u0430\n"
"    10000", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u044b\u043b\u044c \u0432 \n"
"      \u0447\u0430\u0441\n"
"     1000", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.pushButton.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"$hop", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Clicks", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"+ 1 \u0437\u0430 \u043a\u043b\u0438\u043a", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"+ 2 \u0437\u0430 \u043a\u043b\u0438\u043a", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"+ 3 \u0437\u0430 \u043a\u043b\u0438\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Boosters", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Auto-clicks", None))
    # retranslateUi

