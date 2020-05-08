import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from register import Ui_RegisterWindow
from SqlHelper import SqlHelper

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = SqlHelper()

        self.setObjectName("MainWindow")
        self.resize(554, 372)
        self.setMinimumSize(QtCore.QSize(554, 372))
        self.setMaximumSize(QtCore.QSize(554, 372))
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 401, 41))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 110, 421, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.homeRegisterButton = QtWidgets.QPushButton(self.frame)
        self.homeRegisterButton.setGeometry(QtCore.QRect(100, 140, 121, 31))
        self.homeRegisterButton.setObjectName("homeRegisterButton")
        self.homeRegisterButton.setFont(QFont("arial", 11))
        self.homeLoginButton = QtWidgets.QPushButton(self.frame)
        self.homeLoginButton.setGeometry(QtCore.QRect(240, 140, 121, 31))
        self.homeLoginButton.setObjectName("homeLoginButton")
        self.homeLoginButton.clicked.connect(self.loginbtnclicked)
        self.homeLoginButton.setFont(QFont("arial", 11))
        self.homeRegisterButton.clicked.connect(self.regWindow)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.returnPressed.connect(self.loginbtnclicked)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 71, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFocus()
        self.lineEdit.returnPressed.connect(self.onPress)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 71, 31))
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def onPress(self):
        self.lineEdit_2.setFocus(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Welcome"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#484848;\">Welcome to Corona Info App</span></p></body></html>"))
        self.homeRegisterButton.setText(_translate("MainWindow", "Register"))
        self.homeLoginButton.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Password</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Username</span></p></body></html>"))

    def regWindow(self):
        self.w = Ui_RegisterWindow()
        self.w.show()
        self.close()

    def loginbtnclicked(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == "" or password == "":
            if username == "":
                Ui_RegisterWindow().showerror("Error", "Enter Username")
                self.lineEdit.setFocus()
            else:
                Ui_RegisterWindow().showerror("Error", "Enter Password")
                self.lineEdit_2.setFocus()
        else:
            self.tryLogin(username, password)

    def tryLogin(self, username, password):
        if not self.db.userExist(username):
            Ui_RegisterWindow().showerror("Error", "Username not found!")

        else:
            if self.db.checkPassword(username, password):
                print("loggin success")
            else:
                print("error password")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())