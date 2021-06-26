from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, seeker):
        self.MainWindow = MainWindow
        self.seeker = seeker
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1065, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 40, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 120, 1011, 561))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineSearch = QtWidgets.QLineEdit(self.tab)
        self.lineSearch.setGeometry(QtCore.QRect(30, 110, 191, 29))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineSearch.setFont(font)
        self.lineSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSearch.setObjectName("lineSearch")
        self.btnSearch = QtWidgets.QPushButton(self.tab)
        self.btnSearch.setGeometry(QtCore.QRect(31, 150, 63, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.btnSearch.setFont(font)
        self.btnSearch.setStyleSheet("QPushButton {\n"
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
        self.btnSearch.setObjectName("btnSearch")
        self.comboLocation = QtWidgets.QComboBox(self.tab)
        self.comboLocation.setGeometry(QtCore.QRect(31, 220, 191, 29))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.comboLocation.setFont(font)
        self.comboLocation.setObjectName("comboLocation")
        self.btnType = QtWidgets.QPushButton(self.tab)
        self.btnType.setGeometry(QtCore.QRect(31, 390, 118, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.btnType.setFont(font)
        self.btnType.setStyleSheet("QPushButton {\n"
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
        self.btnType.setObjectName("btnType")
        self.comboType = QtWidgets.QComboBox(self.tab)
        self.comboType.setGeometry(QtCore.QRect(31, 340, 191, 29))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.comboType.setFont(font)
        self.comboType.setObjectName("comboType")
        self.btnLocation = QtWidgets.QPushButton(self.tab)
        self.btnLocation.setGeometry(QtCore.QRect(31, 270, 147, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.btnLocation.setFont(font)
        self.btnLocation.setStyleSheet("QPushButton {\n"
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
        self.btnLocation.setObjectName("btnLocation")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(31, 322, 189, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(31, 202, 189, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(30, 90, 189, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(230, 0, 20, 511))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.btnAllJobs = QtWidgets.QPushButton(self.tab)
        self.btnAllJobs.setGeometry(QtCore.QRect(30, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.btnAllJobs.setFont(font)
        self.btnAllJobs.setStyleSheet("QPushButton {\n"
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
        self.btnAllJobs.setObjectName("btnAllJobs")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(250, 10, 741, 441))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btnApply = QtWidgets.QPushButton(self.tab)
        self.btnApply.setGeometry(QtCore.QRect(830, 460, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(18)
        self.btnApply.setFont(font)
        self.btnApply.setStyleSheet("QPushButton {\n"
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
        self.btnApply.setObjectName("btnApply")
        self.labelJobName = QtWidgets.QLabel(self.tab)
        self.labelJobName.setGeometry(QtCore.QRect(420, 460, 391, 40))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(18)
        self.labelJobName.setFont(font)
        self.labelJobName.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelJobName.setObjectName("labelJobName")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEducation = QtWidgets.QLineEdit(self.tab_2)
        self.lineEducation.setGeometry(QtCore.QRect(363, 68, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineEducation.setFont(font)
        self.lineEducation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEducation.setObjectName("lineEducation")
        self.ll1 = QtWidgets.QLabel(self.tab_2)
        self.ll1.setGeometry(QtCore.QRect(203, 70, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(22)
        self.ll1.setFont(font)
        self.ll1.setObjectName("ll1")
        self.lineSkills = QtWidgets.QLineEdit(self.tab_2)
        self.lineSkills.setGeometry(QtCore.QRect(363, 118, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineSkills.setFont(font)
        self.lineSkills.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSkills.setObjectName("lineSkills")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(203, 120, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(203, 172, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineFName_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineFName_7.setGeometry(QtCore.QRect(363, 170, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineFName_7.setFont(font)
        self.lineFName_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineFName_7.setObjectName("lineFName_7")
        self.lineExperience = QtWidgets.QLineEdit(self.tab_2)
        self.lineExperience.setGeometry(QtCore.QRect(363, 218, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineExperience.setFont(font)
        self.lineExperience.setAlignment(QtCore.Qt.AlignCenter)
        self.lineExperience.setObjectName("lineExperience")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(203, 220, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(22)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineBio = QtWidgets.QPlainTextEdit(self.tab_2)
        self.lineBio.setGeometry(QtCore.QRect(363, 270, 381, 121))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineBio.setFont(font)
        self.lineBio.setPlainText("")
        self.lineBio.setPlaceholderText("")
        self.lineBio.setObjectName("lineBio")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(203, 270, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(22)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.btnAddPortfolio = QtWidgets.QPushButton(self.tab_2)
        self.btnAddPortfolio.setGeometry(QtCore.QRect(600, 410, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.btnAddPortfolio.setFont(font)
        self.btnAddPortfolio.setStyleSheet("QPushButton {\n"
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
        self.btnAddPortfolio.setObjectName("btnAddPortfolio")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 40, 431, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineFName = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineFName.setFont(font)
        self.lineFName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineFName.setObjectName("lineFName")
        self.verticalLayout.addWidget(self.lineFName)
        self.lineLName = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineLName.setFont(font)
        self.lineLName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineLName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineLName.setObjectName("lineLName")
        self.verticalLayout.addWidget(self.lineLName)
        self.lineEmail = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineEmail.setFont(font)
        self.lineEmail.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEmail.setObjectName("lineEmail")
        self.verticalLayout.addWidget(self.lineEmail)
        self.linePhone = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.linePhone.setFont(font)
        self.linePhone.setAlignment(QtCore.Qt.AlignCenter)
        self.linePhone.setObjectName("linePhone")
        self.verticalLayout.addWidget(self.linePhone)
        self.lineCurrentPassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineCurrentPassword.setFont(font)
        self.lineCurrentPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineCurrentPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.lineCurrentPassword.setObjectName("lineCurrentPassword")
        self.verticalLayout.addWidget(self.lineCurrentPassword)
        self.linePassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.linePassword.setFont(font)
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linePassword.setAlignment(QtCore.Qt.AlignCenter)
        self.linePassword.setObjectName("linePassword")
        self.verticalLayout.addWidget(self.linePassword)
        self.lineRPassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineRPassword.setFont(font)
        self.lineRPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineRPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.lineRPassword.setObjectName("lineRPassword")
        self.verticalLayout.addWidget(self.lineRPassword)
        self.btnUpdateInfo = QtWidgets.QPushButton(self.tab_3)
        self.btnUpdateInfo.setGeometry(QtCore.QRect(590, 440, 118, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.btnUpdateInfo.setFont(font)
        self.btnUpdateInfo.setStyleSheet("QPushButton {\n"
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
        self.btnUpdateInfo.setObjectName("btnUpdateInfo")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(20, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
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

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "INTERNSHIP APPLICATION"))
        self.lineSearch.setPlaceholderText(_translate("MainWindow", "enter something"))
        self.btnSearch.setText(_translate("MainWindow", "search"))
        self.btnType.setText(_translate("MainWindow", "filter by type"))
        self.btnLocation.setText(_translate("MainWindow", "filter by location"))
        self.btnAllJobs.setText(_translate("MainWindow", "show all internships"))
        self.btnApply.setText(_translate("MainWindow", "apply"))
        self.labelJobName.setText(_translate("MainWindow", "no intership to selected"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "INTERNSHIPS"))
        self.lineEducation.setPlaceholderText(_translate("MainWindow", "education"))
        self.ll1.setText(_translate("MainWindow", "EDUCATION"))
        self.lineSkills.setPlaceholderText(_translate("MainWindow", "skills"))
        self.label_4.setText(_translate("MainWindow", "SKILLS"))
        self.label_8.setText(_translate("MainWindow", "HOBBIES"))
        self.lineFName_7.setPlaceholderText(_translate("MainWindow", "hobbies"))
        self.lineExperience.setPlaceholderText(_translate("MainWindow", "experience"))
        self.label_9.setText(_translate("MainWindow", "EXPERIENCE"))
        self.label_10.setText(_translate("MainWindow", "BIO"))
        self.btnAddPortfolio.setText(_translate("MainWindow", "add portfolio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PORTPOLIO"))
        self.lineFName.setPlaceholderText(_translate("MainWindow", "first name"))
        self.lineLName.setPlaceholderText(_translate("MainWindow", "last name"))
        self.lineEmail.setPlaceholderText(_translate("MainWindow", "email"))
        self.linePhone.setPlaceholderText(_translate("MainWindow", "phone number"))
        self.lineCurrentPassword.setPlaceholderText(_translate("MainWindow", "current password"))
        self.linePassword.setPlaceholderText(_translate("MainWindow", "new password"))
        self.lineRPassword.setPlaceholderText(_translate("MainWindow", "repeat password"))
        self.btnUpdateInfo.setText(_translate("MainWindow", "update info"))
        self.label_2.setText(_translate("MainWindow", "account details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "SETTINGS"))


        self.default()


    def default(self):
        self.btnApply.setDisabled(True)
        self.tableWidget.itemSelectionChanged.connect(self.jobSelected)
        self.btnType.clicked.connect(self.filterbyType)
        self.btnLocation.clicked.connect(self.filterbyLocation)
        self.addToComboBox()
        self.btnAllJobs.clicked.connect(self.updateTable)
        self.btnSearch.clicked.connect(self.searchJob)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Title', 'Type', 'Location', 'Sector', 'Description'])
        self.tableWidget.verticalHeader().hide()
        self.updateTable()
        self.btnApply.clicked.connect(self.apply)
        self.settings()
        self.btnUpdateInfo.clicked.connect(self.updateInfo)
        self.btnAddPortfolio.clicked.connect(self.addPortPolio)
        self.btnBack.clicked.connect(self.back)
        self.btnBack.setText("<")


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
    def addPortPolio(self):
        education = self.lineEducation.text()
        experiece = self.lineExperience.text()
        skills = self.lineSkills.text()
        bio = self.lineBio.toPlainText()
        hobbies = self.lineFName_7.text()

        try:
            conn = sqlite3.connect("dbJobPortal.db")
            q = "select id from tblSeeker where username = '" + self.seeker + "'"
            r = conn.execute(q)
            hostID = r.fetchone()[0]

            q = "insert into tblPortfolio(education, skills, hobbies, experience, bio, seekerID) values('"+education+"','"+skills+"','"+hobbies+"','"+experiece+"','"+bio+"','"+str(hostID)+"')"
            conn.execute(q)
            conn.commit()
            conn.close()

            import PyQt5
            msg = PyQt5.QtWidgets.QMessageBox()
            msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
            msg.setText("Success")
            msg.setInformativeText("Portfolio added")
            msg.setWindowTitle("Success")
            msg.exec_()
        except Exception as e:
            print(e)
            pass
    def settings(self):
        q = "Select fname, lname, email, phone, password from tblSeeker where username = '"+ self.seeker+"'"
        import sqlite3
        conn = sqlite3.connect('dbJobPortal.db')
        result = conn.execute(q)
        r = list(result.fetchall()[0])
        self.lineFName.setText(r[0])
        self.lineLName.setText(r[1])
        self.lineEmail.setText(r[2])
        self.linePhone.setText(r[3])
        self.oldPassword = r[4]

    def updateInfo(self):
        import sqlite3
        conn = sqlite3.connect('dbJobPortal.db')
        fname = self.lineFName.text()
        lname = self.lineLName.text()
        email = self.lineEmail.text()
        phone = self.linePhone.text()
        oldPass = self.lineCurrentPassword.text()
        password = self.linePassword.text()
        rpassword = self.lineRPassword.text()

        if (fname.isalpha()):
            if (lname.isalpha()):
                if (phone.isdigit() and len(phone) > 6):
                    import re
                    if (re.match(r"[^@]+@[^@]+\.[^@]+", email)):
                        s = password
                        if (any(x.isupper() for x in s) and any(x.islower() for x in s)
                                and any(x.isdigit() for x in s) and len(s) >= 7 and len(s) <= 11):
                            if (oldPass == self.oldPassword):
                                if (password == rpassword):
                                    try:
                                        conn = sqlite3.connect("dbJobPortal.db")
                                        q = "update tblSeeker set fname = '"+fname+"',lname = '"+lname+"',email = '"+email+"',phone = '"+phone+"',password = '"+password+"' where username = '"+self.seeker+"'"
                                        print(q)
                                        conn.execute(q)
                                        conn.commit()
                                        print("HERE")
                                        import PyQt5
                                        msg = PyQt5.QtWidgets.QMessageBox()
                                        msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
                                        msg.setText("Success")
                                        msg.setInformativeText("Information Updated")
                                        msg.setWindowTitle("Success")
                                        msg.exec_()
                                    except Exception as e:
                                        print(e)
                            else:
                                self.showMessage("Wrong password")
                        else:
                            self.showMessage(
                                "The password needs at least one lowercase, one uppercase and one number. It should be between 7-11 characters")
                    else:
                        self.showMessage("Please enter a valid email address")
                else:
                    self.showMessage("Please enter a valid phone number")
            else:
                self.showMessage("Please enter a valid last name")
        else:
            self.showMessage("Please enter a valid first name")

    def showMessage(self, message):
        import PyQt5
        msg = PyQt5.QtWidgets.QMessageBox()
        msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
    def apply(self):
        conn = sqlite3.connect("dbJobPortal.db")
        q = "select id from tblSeeker where username = '"+self.seeker+"'"
        r = conn.execute(q)
        result = r.fetchone()
        if(len(result)!=0):
            try:
                seekerID = result[0]
                q = "select id from tblPortfolio where seekerID = '"+str(seekerID)+"'"
                r = conn.execute(q)
                number = r.fetchone()
                if(number == None):
                    result = []
                else:
                    result = number
                isAvailable = len(result)
            except Exception as e:
                print(e)

            if(isAvailable > 0):
                jobName = self.labelJobName.text()
                print(jobName)
                if(jobName!="no jobs to show yet"):
                    try:
                        q = "select id,hostID from tblJob where title = '"+jobName+"'"
                        r = conn.execute(q)
                        jobId = r.fetchone()
                        hostID = jobId[1]
                        jobId = jobId[0]
                        q = "insert into tblApplications(jobID, seekerID,hostID, status) values('"+ str(jobId) + "','"+str(seekerID)+ "','"+str(hostID)+"','PENDING')"
                        conn.execute(q)
                        conn.commit()
                        conn.close()
                        import PyQt5
                        msg = PyQt5.QtWidgets.QMessageBox()
                        msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
                        msg.setText("Success")
                        msg.setInformativeText("Applied for the internship successfully")
                        msg.setWindowTitle("Success")
                        msg.exec_()
                    except Exception as e:
                        print(e)
            if(isAvailable == 0):
                self.showMessage("Please add your portfolio first")
    def jobSelected(self):
        self.labelJobName.setText("No internship selected")
        if(self.tableWidget.currentColumn() == 1):
            self.labelJobName.setText(self.tableWidget.currentItem().text())
            self.btnApply.setDisabled(False)
    def addToComboBox(self):
        try:
            conn = sqlite3.connect('dbJobPortal.db')
            q = "select type from tblJob"
            result = conn.execute(q)
            resultt = result.fetchall()
            for i in resultt:
                for r in i:
                    self.comboType.addItem(i[0])

            q = "select location from tblJob"
            result = conn.execute(q)
            resultt = result.fetchall()
            for i in resultt:
                for r in i:
                    self.comboLocation.addItem(i[0])

        except Exception as ee:
            print(ee)
    def filterbyLocation(self):
        title = self.comboLocation.currentText()
        try:
            conn = sqlite3.connect('dbJobPortal.db')
            q = "select * from tblJob where location = '" + title + "'"
            result = conn.execute(q)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

            conn.close()
        except Exception as ee:
            print(ee)

    def filterbyType(self):
        title = self.comboType.currentText()
        try:
            conn = sqlite3.connect('dbJobPortal.db')
            q = "select * from tblJob where type = '" + title + "'"
            result = conn.execute(q)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

            conn.close()
        except Exception as ee:
            print(ee)
    def searchJob(self):
        title = self.lineSearch.text()
        try:
            conn = sqlite3.connect('dbJobPortal.db')
            q = "select * from tblJob where title = '"+title+"'"
            result = conn.execute(q)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(column_data)))

            conn.close()
        except Exception as ee:
            print(ee)
    def updateTable(self):
        try:
            conn = sqlite3.connect('dbJobPortal.db')
            q = "select * from tblJob"
            result = conn.execute(q)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(column_data)))

            conn.close()
        except Exception as ee:
            print(ee)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, "seeker")
    MainWindow.show()
    sys.exit(app.exec_())
