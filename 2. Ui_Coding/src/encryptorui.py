from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import PyPDF2
from PyQt5.QtWidgets import QInputDialog,QFileDialog
sys.path.append(".")
from PyQt5 import QtCore, QtGui, QtWidgets
from encryptor import encryptor

class Ui_EncryptWindow(object):

    def backToHome(self):
        sys.exit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 270)
        MainWindow.setMinimumSize(QtCore.QSize(508, 270))
        MainWindow.setMaximumSize(QtCore.QSize(508, 270))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 511, 241))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 60, 111, 21))
        self.label.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"\n"
"font: bold 10px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 111, 21))
        self.label_2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"\n"
"font: bold 10px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.input_text = QtWidgets.QLineEdit(self.frame)
        self.input_text.setGeometry(QtCore.QRect(160, 60, 261, 20))
        self.input_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_text.setObjectName("input_text")
        self.output_text = QtWidgets.QLineEdit(self.frame)
        self.output_text.setGeometry(QtCore.QRect(160, 100, 261, 20))
        self.output_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_text.setText("")
        self.output_text.setObjectName("output_text")
        self.encrypt_btn = QtWidgets.QPushButton(self.frame)
        self.encrypt_btn.setGeometry(QtCore.QRect(210, 140, 111, 41))
        self.encrypt_btn.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:rgb(131, 237, 253);\n"
"font: bold 14px;\n"
"padding: 6px;\n"
"min-width:10px;")
        self.encrypt_btn.setObjectName("encrypt_btn")


        self.progress_label = QtWidgets.QLabel(self.frame)
        self.progress_label.setGeometry(QtCore.QRect(70, 200, 381, 41))
        self.progress_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progress_label.setTextFormat(QtCore.Qt.AutoText)
        self.progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_label.setObjectName("progress_label")
        self.input_file_select_btn = QtWidgets.QPushButton(self.frame)
        self.input_file_select_btn.setGeometry(QtCore.QRect(430, 60, 50, 21))
        self.input_file_select_btn.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"\n"
"border-color:rgb(131, 237, 253);\n"
"\n"
"padding: 6px;\n"
"min-width:5px;")
        self.input_file_select_btn.setObjectName("input_file_select_btn")
        self.input_file_select_btn_2 = QtWidgets.QPushButton(self.frame)
        self.input_file_select_btn_2.setGeometry(QtCore.QRect(430, 100, 50, 21))
        self.input_file_select_btn_2.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"\n"
"border-color:rgb(131, 237, 253);\n"
"\n"
"padding: 6px;\n"
"min-width:5px;")
        self.input_file_select_btn_2.setObjectName("input_file_select_btn_2")

        self.back_to_home = QtWidgets.QPushButton(self.frame)
        self.back_to_home.setGeometry(QtCore.QRect(40, 140, 101, 41))
        self.back_to_home.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:rgb(131, 237, 253);\n"
"font: bold 14px;\n"
"padding: 6px;\n"
"min-width:10px;")
        self.back_to_home.setObjectName("back_to_home")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.encrypt_btn.clicked.connect(self.encrypt_button_clicked) 

        self.input_file_select_btn.clicked.connect(self.getInputPath)
        self.input_file_select_btn_2.clicked.connect(self.getOutputPath)
        self.back_to_home.clicked.connect(self.backToHome)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encryptor-by Ravi"))
        self.label.setText(_translate("MainWindow", "Input File Name"))
        self.label_2.setText(_translate("MainWindow", "Output File Name"))
        self.encrypt_btn.setText(_translate("MainWindow", "Encrypt"))
        self.progress_label.setText(_translate("MainWindow", "Progress!!"))
        self.input_file_select_btn.setText(_translate("MainWindow", "file^"))
        self.input_file_select_btn_2.setText(_translate("MainWindow", "file^"))
        self.back_to_home.setText(_translate("MainWindow", "Exit"))

    def encrypt_button_clicked(self):
        input_file_name = self.input_text.text()
        output_file_name =self.output_text.text()
        path=os.getcwd()

        if input_file_name=="" or output_file_name=="":
            msg="Please enter a valid file name"
            self.progress_label.setText(msg)
            return


        if ".txt" in input_file_name:
            input_file_name=input_file_name.replace(".txt","")
            
        if ".txt" in output_file_name:
            output_file_name=output_file_name.replace(".txt","")


        obj = encryptor(input_file_name,output_file_name,path)
        msg=obj.func()

        self.progress_label.setText(msg)

    def open_path_box(self):
        filename = QFileDialog.getOpenFileName()
        print(filename[0])
        return filename[0]

    def save_path_box(self):
        filename = QFileDialog.getSaveFileName()
        print(filename[0])
        return filename[0]



    def getInputPath(self):
        
        self.input_text.setText(self.open_path_box())

    def getOutputPath(self):
        self.output_text.setText(self.save_path_box())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_EncryptWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
