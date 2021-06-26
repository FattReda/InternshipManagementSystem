from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    #Setup ui function which basically set ups the user interface

    def setupUi(self, MainWindow):
        #Making the main window a class attribute
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        #Adjucting the screen size
        MainWindow.resize(800, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Declaring a button named btnAdmin
        self.btnAdmin = QtWidgets.QPushButton(self.centralwidget)

        #Setting up the position, height and width of the button
        self.btnAdmin.setGeometry(QtCore.QRect(260, 120, 291, 71))

        #Declaring a font vairabble and setting the font of the button
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(36)
        self.btnAdmin.setFont(font)

        #Using css to stylize the button
        self.btnAdmin.setStyleSheet("QPushButton {\n"
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

        #Setting the object name of the button
        self.btnAdmin.setObjectName("btnAdmin")

        #Declaring a label
        self.label = QtWidgets.QLabel(self.centralwidget)

        #Setting up the postition, height and width of th e label
        self.label.setGeometry(QtCore.QRect(170, 30, 481, 61))

        #Font as mentioned above
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(48)
        #Changing the font of the label
        self.label.setFont(font)

        #Setting its object name
        self.label.setObjectName("label")

        #Delcaring and placing another button named btnSeeker

        #And setting it up
        self.btnSeeker = QtWidgets.QPushButton(self.centralwidget)
        self.btnSeeker.setGeometry(QtCore.QRect(260, 220, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(36)
        self.btnSeeker.setFont(font)
        self.btnSeeker.setStyleSheet("QPushButton {\n"
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

        #same for this button too, set object name
        self.btnSeeker.setObjectName("btnSeeker")
        self.btnHost = QtWidgets.QPushButton(self.centralwidget)

        #Placing another button and adjusting its font and applying css
        self.btnHost.setGeometry(QtCore.QRect(260, 320, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(36)
        self.btnHost.setFont(font)
        self.btnHost.setStyleSheet("QPushButton {\n"
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
        self.btnHost.setObjectName("btnHost")

        self.btnCreate = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreate.setGeometry(QtCore.QRect(170, 420, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(36)
        self.btnCreate.setFont(font)
        self.btnCreate.setStyleSheet("QPushButton {\n"
" color:white;\n"
"background:#282828;\n"
"    border: 0px solid;\n"
"    border-radius: 2px;\n"
"    border-style: outset;\n"
" \n"
"    }\n"
"QPushButton:pressed {\n"
"    background: white;\n"
"color:black;\n"
"    border: 2px solid #555;\n"
"    border-radius: 4px;\n"
"    border-style: outset;\n"
"  \n"
"    padding: 5px;\n"
"    }")
        self.btnCreate.setObjectName("btnCreate")
        MainWindow.setCentralWidget(self.centralwidget)
        #Calling a retranslate UI function which basically sets the default text on the button
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #Function to set the default text on the buttons
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAdmin.setText(_translate("MainWindow", "ADMIN"))
        self.label.setText(_translate("MainWindow", "INTERNSHIP APPLICATION"))
        self.btnSeeker.setText(_translate("MainWindow", "CANDIDATE"))
        self.btnHost.setText(_translate("MainWindow", "SUPERVISOR"))
        self.btnCreate.setText(_translate("MainWindow", "CREATE AN ACCOUNT"))

        #Function that defines the function calling on particular button clicks
        self.defineClcks()

    # Function that defines the function calling on particular button clicks
    def defineClcks(self):
        self.btnAdmin.clicked.connect(self.admin)
        self.btnHost.clicked.connect(self.host)
        self.btnSeeker.clicked.connect(self.seeker)
        self.btnCreate.clicked.connect(self.create)

    #Admin function for the admin button click basically shows the admin window
    def admin(self):
        try:
            self.window = QtWidgets.QMainWindow()
            from admin import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(e)

    # Seeker function for the seeker button click basically shows the seeker window
    def seeker(self):
        try:
            self.window = QtWidgets.QMainWindow()
            from login import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window, "Seeker")
            self.MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(e)


    # Create function for the create new account button click basically shows the sign up window

    def create(self):
        try:
            self.window = QtWidgets.QMainWindow()
            from signup import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.MainWindow.hide()
            self.window.show()
        except Exception as e:
            print(e)

    # Host function for the host button click basically shows the host window
    def host(self):
        try:
            self.window = QtWidgets.QMainWindow()
            from login import Ui_MainWindow
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window, "Host")
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
