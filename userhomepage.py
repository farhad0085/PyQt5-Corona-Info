import sys
import web
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ui_MainUserWindow(QMainWindow):
    def __init__(self, username):
        #print(username)
        super().__init__()

        self.userfullname = self.get_user_fullname(username)

        self.setObjectName("MainUserWindow")
        self.resize(671, 481)
        self.setMinimumSize(QtCore.QSize(671, 481))
        self.setMaximumSize(QtCore.QSize(671, 481))
        self.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 331, 31))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(11)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(170, 70, 471, 381))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 281, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 131, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 150, 131, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 131, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 230, 131, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 270, 131, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 310, 131, 31))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(210, 70, 221, 31))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(210, 110, 221, 31))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(210, 150, 221, 31))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(210, 190, 221, 31))
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(210, 230, 221, 31))
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(210, 270, 221, 31))
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(210, 310, 221, 31))
        self.label_16.setObjectName("label_16")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 200, 131, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setFocus()
        self.lineEdit_8.returnPressed.connect(self.get_data)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 240, 131, 31))
        self.pushButton_3.clicked.connect(self.get_data)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainUserWindow", "Live Updates!"))
        self.label.setText(_translate("MainUserWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#4b4b4b;\">Welcome "+self.userfullname+"</span></p></body></html>"))
        self.label_2.setText(_translate("MainUserWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Country</span></p></body></html>"))
        self.label_3.setText(_translate("MainUserWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Total Cases</span></p></body></html>"))
        self.label_4.setText(_translate("MainUserWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">New Cases</span></p></body></html>"))
        self.label_5.setText(_translate("MainUserWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Total Deaths</span></p></body></html>"))
        self.label_6.setText(_translate("MainUserWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">New Deaths</span></p></body></html>"))
        self.label_7.setText(_translate("MainUserWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Total Recovered</span></p></body></html>"))
        self.label_8.setText(_translate("MainUserWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Active Cases</span></p></body></html>"))
        self.label_9.setText(_translate("MainUserWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Critical Condition</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainUserWindow", "Quit"))
        self.lineEdit_8.setPlaceholderText(_translate("MainUserWindow", "Country Name..."))
        self.pushButton_3.setText(_translate("MainUserWindow", "View Stats"))

    def get_user_fullname(self, username):
        from SqlHelper import SqlHelper
        db = SqlHelper()
        return db.get_fullName(username)

    def get_data(self):
        if not self.lineEdit_8.text() == "":
            data = web.get_stats(self.lineEdit_8.text())
            if not len(data) == 0:
                self.set_value(data)
            else:
                from register import Ui_RegisterWindow
                Ui_RegisterWindow().showerror("Error", "Country data not found")

    def set_value(self, data):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainUserWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">"
                                        + data[0] + "</span></p></body></html>"))

        self.label_10.setText(_translate("MainUserWindow",
                                         "<html><head/><body><p><span style=\" font-size:11pt;\">"
                                         + data[1] + "</span></p></body></html>"))
        self.label_11.setText(_translate("MainUserWindow",
                                         "<html><head/><body><p><span style=\" font-size:11pt;\">"
                                         + data[2] + "</span></p></body></html>"))
        self.label_12.setText(_translate("MainUserWindow",
                                         "<html><head/><body><p><span style=\" font-size:11pt;\">"
                                         + data[3] + "</span></p></body></html>"))
        self.label_13.setText(_translate("MainUserWindow",
                                         "<html><head/><body><p><span style=\" font-size:11pt;\">"
                                         + data[4] + "</span></p></body></html>"))
        self.label_14.setText(_translate("MainUserWindow",
                                         "<html><head/><body><p><span style=\" font-size:11pt;\">"
                                         + data[5] + "</span></p></body></html>"))
        self.label_15.setText(_translate("MainUserWindow",
                                         "<html><head/><body><p><span style=\" font-size:11pt;\">"
                                         + data[6] + "</span></p></body></html>"))
        self.label_16.setText(_translate("MainUserWindow",
                                         "<html><head/><body><p><span style=\" font-size:11pt;\">"
                                         + data[7] + "</span></p></body></html>"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainUserWindow()
    window.show()
    sys.exit(app.exec())