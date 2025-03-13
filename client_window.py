from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.input_style="background-color:#f5f5f5;\n"\
                         "border:1px solid #e5e5e5;\n"\
                         "border-radius:10px;\n"\
                         "padding:15px;"
        self.pick_style="background-color:#ff8f35;\n"\
                        "border:none;\n"\
                        "border-radius:10px;\n"\
                        "color:black;\n"\
                        "font-family:Calibri;\n"\
                        "font-weight:bold;\n"\
                        "font-size:30px;"
        self.send_style="background-color:green;\n"\
                        "border:none;\n"\
                        "border-radius:10px;\n"\
                        "color:white;\n"\
                        "font-family:Calibri;\n"\
                        "font-weight:bold;\n"\
                        "font-size:30px;"
        self.setObjectName("MainWindow")
        self.resize(800, 900)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.ip = QLineEdit(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(10, 89, 611, 60))
        self.ip.setStyleSheet(self.input_style)
        self.ip.setText("")
        self.ip.setObjectName("ip")
        self.port = QLineEdit(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(640, 90, 113, 60))
        self.port.setStyleSheet(self.input_style)
        self.port.setText("")
        self.port.setObjectName("port")
        self.colon = QLabel(self.centralwidget)
        self.colon.setGeometry(QtCore.QRect(630, 105, 16, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.colon.setFont(font)
        self.colon.setObjectName("colon")
        self.pick = QPushButton(self.centralwidget)
        self.pick.setGeometry(QtCore.QRect(70, 200, 211, 131))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pick.setFont(font)
        self.pick.setStyleSheet(self.pick_style)
        self.pick.setObjectName("pick")
        self.send = QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(340, 200, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setStyleSheet(self.send_style)
        self.send.setObjectName("send")
        self.title = QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ip.setPlaceholderText(_translate("MainWindow", "IP"))
        self.port.setPlaceholderText(_translate("MainWindow", "port (e.g. 12345)"))
        self.colon.setText(_translate("MainWindow", ":"))
        self.pick.setText(_translate("MainWindow", "pick file"))
        self.send.setText(_translate("MainWindow", "send"))
        self.title.setText(_translate("MainWindow", "Image Send"))

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())