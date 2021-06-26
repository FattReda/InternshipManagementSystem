#Importing necassary modules
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #Setting up the user interface
        #Defining buttons, labels, line edits etc.
        #Also this function stylize the buttons using css

        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 30, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(200, 590, 161, 51))
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
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(480, 590, 151, 51))
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
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 170, 431, 391))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineFName = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineFName.setFont(font)
        self.lineFName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineFName.setObjectName("lineFName")
        self.verticalLayout.addWidget(self.lineFName)
        self.lineLName = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineLName.setFont(font)
        self.lineLName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineLName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineLName.setObjectName("lineLName")
        self.verticalLayout.addWidget(self.lineLName)
        self.lineEmail = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineEmail.setFont(font)
        self.lineEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEmail.setObjectName("lineEmail")
        self.verticalLayout.addWidget(self.lineEmail)
        self.linePhone = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.linePhone.setFont(font)
        self.linePhone.setAlignment(QtCore.Qt.AlignCenter)
        self.linePhone.setObjectName("linePhone")
        self.verticalLayout.addWidget(self.linePhone)
        self.lineUsername = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineUsername.setFont(font)
        self.lineUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.lineUsername.setObjectName("lineUsername")
        self.verticalLayout.addWidget(self.lineUsername)
        self.linePassword = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.linePassword.setFont(font)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setAlignment(QtCore.Qt.AlignCenter)
        self.linePassword.setObjectName("linePassword")
        self.verticalLayout.addWidget(self.linePassword)
        self.lineRPassword = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineRPassword.setFont(font)
        self.lineRPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineRPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.lineRPassword.setObjectName("lineRPassword")
        self.verticalLayout.addWidget(self.lineRPassword)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(200, 120, 431, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnLogin.clicked.connect(self.signUp)

    # Signup function for the sign up button click basically shows the login window after creating an account
    def signUp(self):
        import sqlite3
        conn = sqlite3.connect('dbJobPortal.db')
        #Getting the values from line edits and combo boxes
        accountType = self.comboBox.currentText()
        fname = self.lineFName.text()
        lname = self.lineLName.text()
        email = self.lineEmail.text()
        phone = self.linePhone.text()
        username = self.lineUsername.text()
        password = self.linePassword.text()
        rpassword = self.lineRPassword.text()

        #Validating the inputs and after that putting the data in database and continue to login screen

        if(fname.isalpha()):
            if(lname.isalpha()):
                if(phone.isdigit() and len(phone) > 6):
                    import re
                    if(re.match(r"[^@]+@[^@]+\.[^@]+", email)):
                        s = password
                        if (any(x.isupper() for x in s) and any(x.islower() for x in s)
                                and any(x.isdigit() for x in s) and len(s) >= 7 and len(s) <= 11):
                            if(password == rpassword):
                                if(self.comboBox.currentText() == "Supervisor"):
                                    try:
                                        r = conn.execute("select * from tblHost where username = '"+username+"'")
                                        result = r.fetchall()
                                        if(len(result) == 0):
                                            q = "insert into tblHost(fname, lname, email, phone, username, password) values('"+fname+"','"+lname+"','"+email+"','"+phone+"','"+username+"','"+password+"')"
                                            conn.execute(q)
                                            conn.commit()
                                            conn.close()
                                            msg = PyQt5.QtWidgets.QMessageBox()
                                            msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
                                            msg.setText("Success")
                                            msg.setInformativeText("Account created successfully")
                                            msg.setWindowTitle("Success")
                                            msg.exec_()
                                            try:
                                                self.window = QtWidgets.QMainWindow()
                                                from login import Ui_MainWindow
                                                self.ui = Ui_MainWindow()
                                                self.ui.setupUi(self.window, "Host")
                                                self.MainWindow.hide()
                                                self.window.show()
                                            except Exception as e:
                                                print(e)
                                        else:
                                            self.showMessage("Username is already taken")
                                    except Exception as e:
                                        print(e)

                                if(self.comboBox.currentText() == "Internship Candidate"):
                                    try:
                                        r = conn.execute("select * from tblSeeker where username = '"+username+"'")
                                        result = r.fetchall()
                                        if(len(result) == 0):
                                            q = "insert into tblSeeker(fname, lname, email, phone, username, password) values('"+fname+"','"+lname+"','"+email+"','"+phone+"','"+username+"','"+password+"')"
                                            conn.execute(q)
                                            conn.commit()
                                            conn.close()
                                            msg = PyQt5.QtWidgets.QMessageBox()
                                            msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
                                            msg.setText("Success")
                                            msg.setInformativeText("Account created successfully")
                                            msg.setWindowTitle("Success")
                                            msg.exec_()
                                            try:
                                                self.window = QtWidgets.QMainWindow()
                                                from login import Ui_MainWindow
                                                self.ui = Ui_MainWindow()
                                                self.ui.setupUi(self.window, "Job Seeker")
                                                self.MainWindow.hide()
                                                self.window.show()
                                            except Exception as e:
                                                print(e)
                                        else:
                                            self.showMessage("Username is already taken")
                                    except Exception as e:
                                        print(e)
                            else:
                                self.showMessage("Repeat password and password do not match")
                        else:
                            self.showMessage("The password needs at least one lowercase, one uppercase and one number. It should be between 7-11 characters")
                    else:
                        self.showMessage("Please enter a valid email address")
                else:
                    self.showMessage("Please enter a valid phone number")
            else:
                self.showMessage("Please enter a valid last name")
        else:
            self.showMessage("Please enter a valid first name")

    # back function for the back button click basically shows the main window
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

    #Function to show error message
    def showMessage(self, message):
        msg = PyQt5.QtWidgets.QMessageBox()
        msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    #Retransalte function is used to set the default text and setup a ui
    def retranslateUi(self, MainWindow):
        self.btnBack.clicked.connect(self.back)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CREATE NEW ACCOUNT"))
        self.btnBack.setText(_translate("MainWindow", "BACK"))
        self.btnLogin.setText(_translate("MainWindow", "SIGN UP"))
        self.lineFName.setPlaceholderText(_translate("MainWindow", "first name"))
        self.lineLName.setPlaceholderText(_translate("MainWindow", "last name"))
        self.lineEmail.setPlaceholderText(_translate("MainWindow", "email"))
        self.linePhone.setPlaceholderText(_translate("MainWindow", "phone number"))
        self.lineUsername.setPlaceholderText(_translate("MainWindow", "username"))
        self.linePassword.setPlaceholderText(_translate("MainWindow", "password"))
        self.lineRPassword.setPlaceholderText(_translate("MainWindow", "repeat password"))
        self.label_2.setText(_translate("MainWindow", "Choose account type:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Supervisor"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Internship Candidate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
