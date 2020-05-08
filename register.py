import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QLineEdit)
from SqlHelper import SqlHelper

class Ui_RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = SqlHelper()

        self.setObjectName("RegisterWindow")
        self.resize(441, 486)
        self.setMinimumSize(QtCore.QSize(441, 486))
        self.setMaximumSize(QtCore.QSize(441, 486))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 151, 31))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 70, 381, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(260, 340, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.registerbtnclicked)
        self.pushButton.setFont(QFont("arial", 11))
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 340, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.backtohome)
        self.pushButton_2.setFont(QFont("arial", 11))
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 190, 171, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFont(QFont("arial", 11))
        self.lineEdit_4.returnPressed.connect(self.registerbtnclicked)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 290, 171, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setFont(QFont("arial", 11))
        self.lineEdit_6.returnPressed.connect(self.registerbtnclicked)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 141, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 140, 171, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(QFont("arial", 11))
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_3.returnPressed.connect(self.registerbtnclicked)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 40, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFocus(True)
        self.lineEdit.setFont(QFont("arial", 11))
        self.lineEdit.returnPressed.connect(self.registerbtnclicked)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 90, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(QFont("arial", 11))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.returnPressed.connect(self.registerbtnclicked)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 190, 51, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 101, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 290, 71, 31))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 91, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 240, 171, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setFont(QFont("arial", 11))
        self.lineEdit_5.returnPressed.connect(self.registerbtnclicked)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("RegisterWindow", "Register"))
        self.label.setText(_translate("RegisterWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#323232;\">Register</span></p></body></html>"))
        self.pushButton.setText(_translate("RegisterWindow", "Register"))
        self.pushButton_2.setText(_translate("RegisterWindow", "Cancel"))
        self.label_4.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Confirm Password</span></p></body></html>"))
        self.label_2.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Username</span></p></body></html>"))
        self.label_5.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Email</span></p></body></html>"))
        self.label_6.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.label_7.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Age</span></p></body></html>"))
        self.label_3.setText(_translate("RegisterWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Password</span></p></body></html>"))

    def backtohome(self):
        from main import Ui_MainWindow
        self.w = Ui_MainWindow()
        self.w.show()
        self.close()

    def registerbtnclicked(self):

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confPassword = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        fullName = self.lineEdit_5.text()
        age = self.lineEdit_6.text()

        if password == confPassword and username != "" and password != "" and email != "" and fullName != "" and age != "":
                self.registerUser(username, password, email, fullName, age)
        else:
            if password != confPassword:
                self.showerror("Failed", "Password must be matched")
                self.lineEdit_3.setFocus(True)
            elif username == "":
                self.showerror("Failed", "Enter Username Please")
                self.lineEdit.setFocus(True)
            elif password == "":
                self.showerror("Failed", "Enter Password Please")
                self.lineEdit_2.setFocus(True)
            elif email == "":
                self.showerror("Failed", "Enter Email Please")
                self.lineEdit_4.setFocus(True)
            elif fullName == "":
                self.showerror("Failed", "Enter Your Full Name Please")
                self.lineEdit_5.setFocus(True)
            elif age == "":
                self.showerror("Failed", "Enter Your Age Please")
                self.lineEdit_6.setFocus(True)

    def registerUser(self, username, password, email, fullName, age):
        if self.db.registerUser(username, password, email, fullName, age):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Congrats! You have been registered.")
            msg.setWindowTitle("Congrats!")
            detailed_text = "Username : " + username + "\n" + "Password : You know your password"
            msg.setDetailedText(detailed_text)
            msg.exec_()
            self.backtohome()
        else:
            self.showerror("Failed", "Username already exists!")
            self.lineEdit.clear()
            self.lineEdit.setFocus(True)

    def showerror(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()
        #print("error")