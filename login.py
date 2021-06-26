from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, account):
        self.MainWindow = MainWindow
        self.account = account
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 40, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 200, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(220, 290, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.linePassword.setFont(font)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setAlignment(QtCore.Qt.AlignCenter)
        self.linePassword.setObjectName("linePassword")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(440, 380, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(26)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("QPushButton {\n"
"\n"
"    border: 2px solid #555;\n"
"    border-radius: 4px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:pressed {\n"
" color:white;\n"
"background:#282828;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"    border-style: outset;\n"
" \n"
"    }")
        self.btnLogin.setObjectName("btnLogin")
        self.btnAdmin_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdmin_2.setGeometry(QtCore.QRect(220, 380, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(26)
        self.btnAdmin_2.setFont(font)
        self.btnAdmin_2.setStyleSheet("QPushButton {\n"
"\n"
"    border: 2px solid #555;\n"
"    border-radius: 4px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:pressed {\n"
" color:white;\n"
"background:#282828;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"    border-style: outset;\n"
" \n"
"    }")
        self.btnAdmin_2.setObjectName("btnAdmin_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 130, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.btnAdmin_2.clicked.connect(self.back)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def login(self):
        import sqlite3
        conn = sqlite3.connect("dbJobPortal.db")
        username = self.lineEdit.text()
        password = self.linePassword.text()
        if(self.account == "Seeker"):
            r = conn.execute("select password from tblSeeker where username = '"+username+"'")
            result = r.fetchall()
            if(len(result) == 0):
                import PyQt5
                message = "Invalid username"
                msg = PyQt5.QtWidgets.QMessageBox()
                msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText(message)
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                correctPassword = (result[0])[0]
                if(password == correctPassword):
                    try:
                        self.window = QtWidgets.QMainWindow()
                        from candidate import Ui_MainWindow
                        self.ui = Ui_MainWindow()
                        self.ui.setupUi(self.window, username)
                        self.MainWindow.hide()
                        self.window.show()
                    except Exception as e:
                        print(e)
                else:
                    import PyQt5
                    message = "Invalid credentials"
                    msg = PyQt5.QtWidgets.QMessageBox()
                    msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText(message)
                    msg.setWindowTitle("Error")
                    msg.exec_()
        if(self.account == "Host"):
            r = conn.execute("select password from tblHost where username = '" + username + "'")
            result = r.fetchall()
            if (len(result) == 0):
                import PyQt5
                message = "Invalid username"
                msg = PyQt5.QtWidgets.QMessageBox()
                msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText(message)
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                correctPassword = (result[0])[0]
                if (password == correctPassword):
                    try:
                        self.window = QtWidgets.QMainWindow()
                        from supervisor import Ui_MainWindow
                        self.ui = Ui_MainWindow()
                        self.ui.setupUi(self.window, username)
                        self.MainWindow.hide()
                        self.window.show()
                    except Exception as e:
                        print(e)
                else:
                    import PyQt5
                    message = "Invalid credentials"
                    msg = PyQt5.QtWidgets.QMessageBox()
                    msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText(message)
                    msg.setWindowTitle("Error")
                    msg.exec_()

    def back(self):
        try:
            self.window = QtWidgets.QMainWindow()
            from main import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(e)
    def retranslateUi(self, MainWindow):
        self.btnLogin.clicked.connect(self.login)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LOGIN"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "username"))
        self.linePassword.setPlaceholderText(_translate("MainWindow", "password"))
        self.btnLogin.setText(_translate("MainWindow", "LOGIN"))
        self.btnAdmin_2.setText(_translate("MainWindow", "BACK"))
        self.label_2.setText(_translate("MainWindow", "enter your credentials"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, "Seeker")
    MainWindow.show()
    sys.exit(app.exec_())
