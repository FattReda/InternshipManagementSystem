from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 30, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineSeeker = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSeeker.setGeometry(QtCore.QRect(60, 200, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineSeeker.setFont(font)
        self.lineSeeker.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSeeker.setObjectName("lineSeeker")
        self.btnDeleteSeeker = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteSeeker.setGeometry(QtCore.QRect(110, 260, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(26)
        self.btnDeleteSeeker.setFont(font)
        self.btnDeleteSeeker.setStyleSheet("QPushButton {\n"
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
        self.btnDeleteSeeker.setObjectName("btnDeleteSeeker")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(10, 20, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(26)
        self.btnBack.setFont(font)
        self.btnBack.setStyleSheet("QPushButton {\n"
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
        self.btnBack.setObjectName("btnBack")
        self.lineHost = QtWidgets.QLineEdit(self.centralwidget)
        self.lineHost.setGeometry(QtCore.QRect(430, 200, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineHost.setFont(font)
        self.lineHost.setAlignment(QtCore.Qt.AlignCenter)
        self.lineHost.setObjectName("lineHost")
        self.btnDeleteHost = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteHost.setGeometry(QtCore.QRect(480, 260, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(26)
        self.btnDeleteHost.setFont(font)
        self.btnDeleteHost.setStyleSheet("QPushButton {\n"
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
        self.btnDeleteHost.setObjectName("btnDeleteHost")
        self.addSH = QtWidgets.QPushButton(self.centralwidget)
        self.addSH.setGeometry(QtCore.QRect(210, 410, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(26)
        self.addSH.setFont(font)
        self.addSH.setStyleSheet("QPushButton {\n"
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
        self.addSH.setObjectName("addSH")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ADMIN"))
        self.lineSeeker.setPlaceholderText(_translate("MainWindow", "candidate name"))
        self.btnDeleteSeeker.setText(_translate("MainWindow", "delete candidate"))
        self.btnBack.setText(_translate("MainWindow", "<"))
        self.lineHost.setPlaceholderText(_translate("MainWindow", "supervisor name"))
        self.btnDeleteHost.setText(_translate("MainWindow", "delete supervisor"))
        self.addSH.setText(_translate("MainWindow", "ADD CANDIDATE/SUPERVISOR"))
        self.default()
    def default(self):
        self.btnBack.clicked.connect(self.back)
        self.btnDeleteHost.clicked.connect(self.deleteHost)
        self.btnDeleteSeeker.clicked.connect(self.deleteSeeker)
        self.addSH.clicked.connect(self.addSh)
    def deleteHost(self):
        name = self.lineHost.text()
        print(name)
        try:
            import sqlite3
            conn = sqlite3.connect("dbJobPortal.db")
            q = "delete from tblHost where fname = '"+name+"'"
            r = conn.execute(q)
            conn.commit()
            conn.close()
            row = r.rowcount
            if(row > 0):
                import PyQt5
                msg = PyQt5.QtWidgets.QMessageBox()
                msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
                msg.setText("Success")
                msg.setInformativeText("Host "+name+" delete successfully")
                msg.setWindowTitle("Success")
                msg.exec_()
            if(row == 0):
                self.showMessage("Host with this name not found")
        except Exception as e:
            print(e)
            self.showMessage("Host with this name not found")

    def deleteSeeker(self):
        name = self.lineSeeker.text()
        print(name)
        try:
            import sqlite3
            conn = sqlite3.connect("dbJobPortal.db")
            q = "delete from tblSeeker where fname = '" + name + "'"
            r = conn.execute(q)
            conn.commit()
            conn.close()
            row = r.rowcount
            if (row > 0):
                import PyQt5
                msg = PyQt5.QtWidgets.QMessageBox()
                msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
                msg.setText("Success")
                msg.setInformativeText("Seeker " + name + " delete successfully")
                msg.setWindowTitle("Success")
                msg.exec_()
            if (row == 0):
                self.showMessage("Seeker with this name not found")
        except Exception as e:
            print(e)
            self.showMessage("Seeker with this name not found")
    def showMessage(self, message):
        import PyQt5
        msg = PyQt5.QtWidgets.QMessageBox()
        msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
    def addSh(self):
        try:
            self.window = QtWidgets.QMainWindow()
            from signup import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(e)
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
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
