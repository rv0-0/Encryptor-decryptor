# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from encryptorui import Ui_EncryptWindow
from decryptorui import Ui_DecryptWindow
import sys

class Ui_MainWindow(object):
    

    def openDecryptor(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_DecryptWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def exitWindow(self):
        sys.exit()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(409, 363)
        MainWindow.setMinimumSize(QtCore.QSize(409, 363))
        MainWindow.setMaximumSize(QtCore.QSize(409, 363))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Decryptor = QtWidgets.QPushButton(self.centralwidget)
        self.Decryptor.setGeometry(QtCore.QRect(140, 170, 111, 71))
        self.Decryptor.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:rgb(131, 237, 253);\n"
"font: bold 14px;\n"
"padding: 6px;\n"
"min-width:10px;")
        self.Decryptor.setObjectName("Decryptor")
        self.Encryptor = QtWidgets.QPushButton(self.centralwidget)
        self.Encryptor.setGeometry(QtCore.QRect(140, 80, 111, 71))
        self.Encryptor.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:rgb(131, 237, 253);\n"
"font: bold 14px;\n"
"padding: 6px;\n"
"min-width:10px;")
        self.Encryptor.setObjectName("Encryptor")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(140, 260, 111, 71))
        self.Exit.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:rgb(131, 237, 253);\n"
"font: bold 14px;\n"
"padding: 6px;\n"
"min-width:10px;")
        self.Exit.setObjectName("Exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 301, 41))
        self.label.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"\n"
"\n"
"font: bold 14px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Decryptor.clicked.connect(self.openDecryptor)
        self.Encryptor.clicked.connect(self.openEncryptor )
        self.Exit.clicked.connect(self.exitWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Home-by Ravi"))
        self.Decryptor.setText(_translate("MainWindow", "Decryptor"))
        self.Encryptor.setText(_translate("MainWindow", "Encryptor"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "ENCRYPTOR DECRYPTOR"))
    def openEncryptor(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_EncryptWindow()
        self.ui.setupUi(self.window)
        self.window.show()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
