# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Screen = QtWidgets.QLabel(self.centralwidget)
        self.Screen.setGeometry(QtCore.QRect(40, 20, 351, 291))
        self.Screen.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.Screen.setFrameShape(QtWidgets.QFrame.Box)
        self.Screen.setLineWidth(3)
        self.Screen.setText("")
        self.Screen.setScaledContents(True)
        self.Screen.setObjectName("Screen")
        self.line_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Edit.setGeometry(QtCore.QRect(30, 430, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_Edit.setFont(font)
        self.line_Edit.setObjectName("line_Edit")
        self.Browser_button = QtWidgets.QPushButton(self.centralwidget)
        self.Browser_button.setGeometry(QtCore.QRect(534, 430, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Browser_button.setFont(font)
        self.Browser_button.setObjectName("Browser_button")
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(160, 330, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Start_Button.setFont(font)
        self.Start_Button.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.Start_Button.setObjectName("Start_Button")
        self.Name_1 = QtWidgets.QLabel(self.centralwidget)
        self.Name_1.setGeometry(QtCore.QRect(420, 60, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Name_1.setFont(font)
        self.Name_1.setFrameShape(QtWidgets.QFrame.Box)
        self.Name_1.setLineWidth(3)
        self.Name_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Name_1.setObjectName("Name_1")
        self.Percent_1 = QtWidgets.QLabel(self.centralwidget)
        self.Percent_1.setGeometry(QtCore.QRect(630, 60, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Percent_1.setFont(font)
        self.Percent_1.setFrameShape(QtWidgets.QFrame.Box)
        self.Percent_1.setLineWidth(2)
        self.Percent_1.setObjectName("Percent_1")
        self.Percent_2 = QtWidgets.QLabel(self.centralwidget)
        self.Percent_2.setGeometry(QtCore.QRect(630, 120, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Percent_2.setFont(font)
        self.Percent_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Percent_2.setLineWidth(2)
        self.Percent_2.setObjectName("Percent_2")
        self.Name_2 = QtWidgets.QLabel(self.centralwidget)
        self.Name_2.setGeometry(QtCore.QRect(420, 120, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Name_2.setFont(font)
        self.Name_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Name_2.setLineWidth(3)
        self.Name_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Name_2.setObjectName("Name_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Browser_button.setText(_translate("MainWindow", "Browser"))
        self.Start_Button.setText(_translate("MainWindow", "Start"))
        self.Name_1.setText(_translate("MainWindow", "Name 1"))
        self.Percent_1.setText(_translate("MainWindow", "%"))
        self.Percent_2.setText(_translate("MainWindow", "%"))
        self.Name_2.setText(_translate("MainWindow", "Name 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
