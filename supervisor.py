from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, host):
        self.host = host
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 780, 571))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineSearch_2 = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineSearch_2.setFont(font)
        self.lineSearch_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSearch_2.setObjectName("lineSearch_2")
        self.verticalLayout_2.addWidget(self.lineSearch_2)
        self.lineType = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineType.setFont(font)
        self.lineType.setAlignment(QtCore.Qt.AlignCenter)
        self.lineType.setObjectName("lineType")
        self.verticalLayout_2.addWidget(self.lineType)
        self.lineSector = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineSector.setFont(font)
        self.lineSector.setAlignment(QtCore.Qt.AlignCenter)
        self.lineSector.setObjectName("lineSector")
        self.verticalLayout_2.addWidget(self.lineSector)
        self.lineLocation = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineLocation.setFont(font)
        self.lineLocation.setAlignment(QtCore.Qt.AlignCenter)
        self.lineLocation.setObjectName("lineLocation")
        self.verticalLayout_2.addWidget(self.lineLocation)
        self.lineDescription = QtWidgets.QPlainTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineDescription.setFont(font)
        self.lineDescription.setObjectName("lineDescription")
        self.verticalLayout_2.addWidget(self.lineDescription)
        self.btnAddJob = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(18)
        self.btnAddJob.setFont(font)
        self.btnAddJob.setStyleSheet("QPushButton {\n"
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
        self.btnAddJob.setObjectName("btnAddJob")
        self.verticalLayout_2.addWidget(self.btnAddJob)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tblApplocations = QtWidgets.QTableWidget(self.tab_2)
        self.tblApplocations.setGeometry(QtCore.QRect(20, 10, 731, 441))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.tblApplocations.setFont(font)
        self.tblApplocations.setObjectName("tblApplocations")
        self.tblApplocations.setColumnCount(0)
        self.tblApplocations.setRowCount(0)

        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(22)

        self.labelApplicantName = QtWidgets.QLabel(self.tab_2)
        self.labelApplicantName.setGeometry(QtCore.QRect(410, 470, 231, 31))
        self.labelApplicantName.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelApplicantName.setObjectName("labelApplicantName")
        self.labelApplicantName.setFont(font)
        self.btnApprove = QtWidgets.QPushButton(self.tab_2)
        self.btnApprove.setGeometry(QtCore.QRect(660, 460, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(18)
        self.btnApprove.setFont(font)
        self.btnApprove.setStyleSheet("QPushButton {\n"
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
        self.btnApprove.setObjectName("btnApprove")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineCompanyName = QtWidgets.QLineEdit(self.tab_4)
        self.lineCompanyName.setGeometry(QtCore.QRect(310, 40, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineCompanyName.setFont(font)
        self.lineCompanyName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineCompanyName.setObjectName("lineCompanyName")
        self.l1 = QtWidgets.QLabel(self.tab_4)
        self.l1.setGeometry(QtCore.QRect(40, 40, 241, 40))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.lineComanyAddress = QtWidgets.QLineEdit(self.tab_4)
        self.lineComanyAddress.setGeometry(QtCore.QRect(310, 90, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineComanyAddress.setFont(font)
        self.lineComanyAddress.setAlignment(QtCore.Qt.AlignCenter)
        self.lineComanyAddress.setObjectName("lineComanyAddress")
        self.l2 = QtWidgets.QLabel(self.tab_4)
        self.l2.setGeometry(QtCore.QRect(40, 90, 241, 40))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(self.tab_4)
        self.l3.setGeometry(QtCore.QRect(40, 140, 241, 40))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.lineComanyNumberEmployees = QtWidgets.QSpinBox(self.tab_4)
        self.lineComanyNumberEmployees.setGeometry(QtCore.QRect(310, 140, 381, 41))
        self.lineComanyNumberEmployees.setObjectName("lineComanyNumberEmployees")
        self.lineComanyNumberVacancies = QtWidgets.QSpinBox(self.tab_4)
        self.lineComanyNumberVacancies.setGeometry(QtCore.QRect(310, 190, 381, 41))
        self.lineComanyNumberVacancies.setObjectName("lineComanyNumberVacancies")
        self.l4 = QtWidgets.QLabel(self.tab_4)
        self.l4.setGeometry(QtCore.QRect(40, 190, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.lineComanyDescription = QtWidgets.QPlainTextEdit(self.tab_4)
        self.lineComanyDescription.setGeometry(QtCore.QRect(310, 240, 381, 181))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.lineComanyDescription.setFont(font)
        self.lineComanyDescription.setObjectName("lineComanyDescription")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(40, 240, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.btnAddPage = QtWidgets.QPushButton(self.tab_4)
        self.btnAddPage.setGeometry(QtCore.QRect(570, 440, 118, 41))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(20)
        self.btnAddPage.setFont(font)
        self.btnAddPage.setStyleSheet("QPushButton {\n"
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
        self.btnAddPage.setObjectName("btnAddPage")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 40, 431, 391))
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
        self.btnUpdateInfo.setGeometry(QtCore.QRect(470, 440, 118, 41))
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
        self.label_2.setGeometry(QtCore.QRect(300, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT Condensed")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
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


    def addJob(self):
        import sqlite3
        title = self.lineSearch_2.text()
        type = self.lineType.text()
        sector = self.lineSector.text()
        location = self.lineLocation.text()
        des = self.lineDescription.toPlainText()
        conn = sqlite3.connect("dbJobPortal.db")
        q = "select id from tblHost where username = '"+self.host+"'"
        r = conn.execute(q)
        hostID = r.fetchone()[0]
        try:
            query = "insert into tblJob(title, description, type, location, sector, hostID) values('"+title+"','"+des+"','"+type+"','"+location+"','"+sector+"','"+str(hostID)+"')"
            conn.execute(query)
            conn.commit()
            conn.close()
            msg = PyQt5.QtWidgets.QMessageBox()
            msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
            msg.setText("Success")
            msg.setInformativeText("Job Added")
            msg.setWindowTitle("Success")
            msg.exec_()
        except Exception as e:
            print(e)

    def candidateSelected(self):
        self.labelApplicantName.setText("No applicant selected")
        if (self.tblApplocations.currentColumn() == 0):
            try:
                id = self.tblApplocations.currentItem().text()
                import sqlite3
                conn = sqlite3.connect("dbJobPortal.db")
                q = "select seekerID from tblPortfolio where id = '"+str(id)+"'"
                r = conn.execute(q)
                seekerID = r.fetchone()[0]
                q = "select fname from tblSeeker where id = '"+str(seekerID)+"'"
                r = conn.execute(q)
                fname = r.fetchone()[0]
                self.candidateName = fname
                self.labelApplicantName.setText("Candidate Name: "+ fname)
            except Exception as e:
                print(e)

    def approve(self):
        applicant = self.candidateName
        if(applicant!=""):
            try:
                q = "select id from tblSeeker where fname = +'"+applicant+"'"
                import sqlite3
                conn = sqlite3.connect('dbJobPortal.db')
                result = conn.execute(q)
                q = "update tblApplications set status = 'APPROVED' where seekerID = '"+str(result.fetchone()[0])+"'"
                conn.execute(q)
                conn.commit()
                msg = PyQt5.QtWidgets.QMessageBox()
                msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
                msg.setText("Success")
                msg.setInformativeText("Applicant approved")
                msg.setWindowTitle("Success")
                msg.exec_()
                self.candidateName = ""
                self.updateTable()
            except Exception as e:
                print(e)
                pass
        if(applicant == ""):
            self.showMessage("Please select a candidate first")
    def updateTable(self):
        try:
            import sqlite3
            conn = sqlite3.connect('dbJobPortal.db')
            q = "select id from tblHost where username = +'"+self.host+"'"
            result = conn.execute(q)
            hostID = result.fetchone()[0]
            q = "select seekerID from tblApplications where hostID = '" + str(hostID) + "' and status = 'PENDING'"
            result = conn.execute(q)

            self.tblApplocations.setRowCount(0)
            for seeker in result.fetchall():
                q = "select * from tblPortfolio where seekerID = '"+str(seeker[0])+"'"
                result = conn.execute(q)
                for row_number, row_data in enumerate(result):
                    self.tblApplocations.insertRow(row_number)
                    for column_number, column_data in enumerate(row_data):
                        self.tblApplocations.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))

            conn.close()
        except Exception as ee:
            print(ee)
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
                                        q = "update tblHost set fname = '"+fname+"',lname = '"+lname+"',email = '"+email+"',phone = '"+phone+"',password = '"+password+"' where username = '"+self.host+"'"
                                        print(q)
                                        conn.execute(q)
                                        conn.commit()

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
    def showMessage(self, message):
        msg = PyQt5.QtWidgets.QMessageBox()
        msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
    def settings(self):
        self.btnBack.clicked.connect(self.back)
        self.btnBack.setText("<")
        q = "Select fname, lname, email, phone, password from tblHost where username = '"+ self.host+"'"
        import sqlite3
        conn = sqlite3.connect('dbJobPortal.db')
        result = conn.execute(q)
        r = list(result.fetchall()[0])
        self.lineFName.setText(r[0])
        self.lineLName.setText(r[1])
        self.lineEmail.setText(r[2])
        self.linePhone.setText(r[3])
        self.oldPassword = r[4]


    def addPage(self):
        name = self.lineCompanyName.text()
        address = self.lineComanyAddress.text()
        employees = self.lineComanyNumberEmployees.text()
        vacancies = self.lineComanyNumberVacancies.text()
        description = self.lineComanyDescription.toPlainText()
        try:
            import sqlite3
            conn = sqlite3.connect("dbJobPortal.db")
            q = "select id from tblHost where username = '" + self.host + "'"
            r = conn.execute(q)
            hostID = r.fetchone()[0]
            q = "insert into tblCompanyPage(name, employees, vacancies, address, description, hostID) values('"+name+"','"+employees+"','"+vacancies+"','"+address+"','"+description+"','"+str(hostID)+"')"
            conn.execute(q)
            conn.commit()
            conn.close()

            msg = PyQt5.QtWidgets.QMessageBox()
            msg.setIcon(PyQt5.QtWidgets.QMessageBox.Information)
            msg.setText("Success")
            msg.setInformativeText("Page created successfully")
            msg.setWindowTitle("Success")
            msg.exec_()
        except Exception as e:
            print(e)
    def retranslateUi(self, MainWindow):
        self.candidateName = ""
        self.btnAddPage.clicked.connect(self.addPage)
        self.btnUpdateInfo.clicked.connect(self.updateInfo)
        self.settings()
        self.tblApplocations.setColumnCount(6)
        self.tblApplocations.setHorizontalHeaderLabels(["ID","Education","Skills", "Hobbies", "Experiece", "Bio"])
        self.tblApplocations.itemSelectionChanged.connect(self.candidateSelected)
        self.tblApplocations.verticalHeader().hide()
        header = self.tblApplocations.horizontalHeader()
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.btnApprove.clicked.connect(self.approve)

        self.updateTable()
        self.btnAddJob.clicked.connect(self.addJob)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineSearch_2.setPlaceholderText(_translate("MainWindow", "internship title"))
        self.lineType.setPlaceholderText(_translate("MainWindow", "internship type"))
        self.lineSector.setPlaceholderText(_translate("MainWindow", "sector"))
        self.lineLocation.setPlaceholderText(_translate("MainWindow", "location"))
        self.lineDescription.setPlaceholderText(_translate("MainWindow", "description"))
        self.btnAddJob.setText(_translate("MainWindow", "add job"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "INTERNSHIPS"))
        self.labelApplicantName.setText(_translate("MainWindow", "No applicant selected"))
        self.btnApprove.setText(_translate("MainWindow", "APPROVE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "APPLICATIONS"))
        self.lineCompanyName.setPlaceholderText(_translate("MainWindow", "comany name"))
        self.l1.setText(_translate("MainWindow", "COMPANY NAME"))
        self.lineComanyAddress.setPlaceholderText(_translate("MainWindow", "address"))
        self.l2.setText(_translate("MainWindow", "COMAPANY ADDRESS"))
        self.l3.setText(_translate("MainWindow", "NUMBER OF TRAINEES"))
        self.l4.setText(_translate("MainWindow", "NUMBER OF VACANCIES"))
        self.lineComanyDescription.setPlaceholderText(_translate("MainWindow", "company description goes here"))
        self.label_7.setText(_translate("MainWindow", "DESCRIPTION"))
        self.btnAddPage.setText(_translate("MainWindow", "add page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "COMPANY PAGE"))
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
        self.label.setText(_translate("MainWindow", "INTERNSHIP APPLICATION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,"asd")
    MainWindow.show()
    sys.exit(app.exec_())
