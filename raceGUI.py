from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

from race import *
from popupMessage import *

raceNameList = []


class Ui_raceNamesGUI(object):
    def setupUi(self, raceNamesGUI):
        raceNamesGUI.setObjectName("raceNamesGUI")
        raceNamesGUI.resize(500, 250)
        self.centralwidget = QtWidgets.QWidget(raceNamesGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.eventNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.eventNameEdit.setGeometry(QtCore.QRect(102, 40, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.eventNameEdit.setFont(font)
        self.eventNameEdit.setObjectName("eventNameEdit")
        self.raceNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.raceNameEdit.setGeometry(QtCore.QRect(102, 70, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.raceNameEdit.setFont(font)
        self.raceNameEdit.setObjectName("raceNameEdit")
        self.nextRaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextRaceButton.setGeometry(QtCore.QRect(280, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nextRaceButton.setFont(font)
        self.nextRaceButton.setObjectName("nextRaceButton")
        self.nextRaceButton.clicked.connect(self.raceNameAsign)

        self.saveAndExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveAndExitButton.setGeometry(QtCore.QRect(390, 160, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveAndExitButton.setFont(font)
        self.saveAndExitButton.setObjectName("saveAndExitButton")
        self.saveAndExitButton.clicked.connect(self.raceNameAsignAndExit)

        self.raceDateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.raceDateEdit.setGeometry(QtCore.QRect(280, 101, 81, 31))
        self.raceDateEdit.setDate(QDate.currentDate())
        self.raceDateEdit.setCalendarPopup(True)
        self.raceDateEdit.setObjectName("raceDateEdit")
        raceNamesGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(raceNamesGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        raceNamesGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(raceNamesGUI)
        self.statusbar.setObjectName("statusbar")
        raceNamesGUI.setStatusBar(self.statusbar)

        self.retranslateUi(raceNamesGUI)
        QtCore.QMetaObject.connectSlotsByName(raceNamesGUI)

    def retranslateUi(self, raceNamesGUI):
        _translate = QtCore.QCoreApplication.translate
        raceNamesGUI.setWindowTitle(_translate("raceNamesGUI", "Define Race Names"))
        self.label.setText(_translate("raceNamesGUI", "Insert Race Name"))
        self.label_2.setText(_translate("raceNamesGUI", "Event Name:"))
        self.label_3.setText(_translate("raceNamesGUI", "Race Name:"))
        self.label_4.setText(_translate("raceNamesGUI", "Race Date"))
        self.nextRaceButton.setText(_translate("raceNamesGUI", "Next Race"))
        self.saveAndExitButton.setText(_translate("raceNamesGUI", "Save and Exit"))
        self.raceDateEdit.setDisplayFormat(_translate("raceNamesGUI", "d/M/yyyy"))

    def raceNameAsign(self):

        en = self.eventNameEdit.text()
        rn = self.raceNameEdit.text()
        rd = self.raceDateEdit.text()

        if en == '':
            popupmessage("Event Name missing!")
            self.eventNameEdit.setFocus()
        elif rn == '':
            popupmessage("Race Name is missing!")
            self.raceNameEdit.setFocus()

        else:
            race = Race(en, rn, rd)
            raceNameList.append(race)
            popupmessage(f'Race {rn} has been saved successfully')
            self.eventNameEdit.clear()
            self.raceNameEdit.clear()
            self.raceDateEdit.setDate(QDate.currentDate())

    def raceNameAsignAndExit(self):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    raceNamesGUI = QtWidgets.QMainWindow()
    ui = Ui_raceNamesGUI()
    ui.setupUi(raceNamesGUI)
    raceNamesGUI.show()
    sys.exit(app.exec_())
