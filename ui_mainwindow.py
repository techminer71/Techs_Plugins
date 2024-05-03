# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledGUlmpQ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollBar, QSizePolicy, QStatusBar, QTableView,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(822, 617)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Plugin_List = QTableView(self.centralwidget)
        self.Plugin_List.setObjectName(u"Plugin_List")
        self.Plugin_List.setGeometry(QRect(10, 40, 471, 321))
        self.Plugin_Info = QTextBrowser(self.centralwidget)
        self.Plugin_Info.setObjectName(u"Plugin_Info")
        self.Plugin_Info.setGeometry(QRect(10, 370, 471, 192))
        self.Plugin_List_Scroll = QScrollBar(self.centralwidget)
        self.Plugin_List_Scroll.setObjectName(u"Plugin_List_Scroll")
        self.Plugin_List_Scroll.setGeometry(QRect(480, 40, 20, 321))
        self.Plugin_List_Scroll.setOrientation(Qt.Orientation.Vertical)
        self.Add_Plugin = QPushButton(self.centralwidget)
        self.Add_Plugin.setObjectName(u"Add_Plugin")
        self.Add_Plugin.setGeometry(QRect(320, 10, 75, 24))
        self.Remove_Sel_Plugin = QPushButton(self.centralwidget)
        self.Remove_Sel_Plugin.setObjectName(u"Remove_Sel_Plugin")
        self.Remove_Sel_Plugin.setGeometry(QRect(400, 10, 75, 24))
        self.Plugin_URL_Field = QLineEdit(self.centralwidget)
        self.Plugin_URL_Field.setObjectName(u"Plugin_URL_Field")
        self.Plugin_URL_Field.setGeometry(QRect(120, 10, 191, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(68, 10, 51, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 822, 33))
        self.menuTech_s_3D_Plugin_Manager = QMenu(self.menubar)
        self.menuTech_s_3D_Plugin_Manager.setObjectName(u"menuTech_s_3D_Plugin_Manager")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTech_s_3D_Plugin_Manager.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Add_Plugin.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.Remove_Sel_Plugin.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plugin ID", None))
        self.menuTech_s_3D_Plugin_Manager.setTitle(QCoreApplication.translate("MainWindow", u"Plugins", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

