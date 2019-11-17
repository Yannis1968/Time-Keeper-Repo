from PyQt5 import QtCore, QtGui, QtWidgets
from category import *
from popupMessage import *

categoryList = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextCategoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextCategoryButton.setGeometry(QtCore.QRect(354, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.nextCategoryButton.setFont(font)
        self.nextCategoryButton.setObjectName("nextCategoryButton")
        self.nextCategoryButton.clicked.connect(self.asignCategory)

        self.saveAndExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveAndExitButton.setGeometry(QtCore.QRect(470, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.saveAndExitButton.setFont(font)
        self.saveAndExitButton.setObjectName("saveAndExitButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 561, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 3, 1, 1, 2)

        self.maleRadioButton = QtWidgets.QRadioButton(self.widget)

        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.maleRadioButton.setFont(font)
        self.maleRadioButton.setObjectName("maleRadioButton")
        self.gridLayout.addWidget(self.maleRadioButton, 4, 1, 1, 1)
        self.maleRadioButton.setChecked(True)
        self.femaleRadioButton = QtWidgets.QRadioButton(self.widget)

        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.femaleRadioButton.setFont(font)
        self.femaleRadioButton.setObjectName("femaleRadioButton")
        self.gridLayout.addWidget(self.femaleRadioButton, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 4)
        self.categoryNameLineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        self.categoryNameLineEdit.setFont(font)
        self.categoryNameLineEdit.setObjectName("categoryNameLineEdit")
        self.gridLayout.addWidget(self.categoryNameLineEdit, 1, 1, 1, 3)
        self.lowerAgeLimitLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lowerAgeLimitLabel.setFont(font)
        self.lowerAgeLimitLabel.setObjectName("lowerAgeLimitLabel")
        self.gridLayout.addWidget(self.lowerAgeLimitLabel, 2, 3, 1, 1)
        self.upperAgeLimitLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.upperAgeLimitLabel.sizePolicy().hasHeightForWidth()
        )
        self.upperAgeLimitLabel.setSizePolicy(sizePolicy)
        self.upperAgeLimitLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.upperAgeLimitLabel.setFont(font)
        self.upperAgeLimitLabel.setObjectName("upperAgeLimitLabel")
        self.gridLayout.addWidget(self.upperAgeLimitLabel, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged["int"].connect(
            self.lowerAgeLimitLabel.setNum
        )
        self.horizontalSlider_2.valueChanged["int"].connect(
            self.upperAgeLimitLabel.setNum
        )
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextCategoryButton.setText(_translate("MainWindow", "Next Category"))
        self.saveAndExitButton.setText(_translate("MainWindow", "Save and Exit"))
        self.label_3.setText(_translate("MainWindow", "Category Name:"))
        self.label.setText(_translate("MainWindow", "Lower Age Limit:"))
        self.label_2.setText(_translate("MainWindow", "Upper Age Limit:"))
        self.maleRadioButton.setText(_translate("MainWindow", "Male"))
        self.femaleRadioButton.setText(_translate("MainWindow", "Female"))
        self.label_4.setText(_translate("MainWindow", "Insert your Categories"))
        self.lowerAgeLimitLabel.setText(_translate("MainWindow", "0"))
        self.upperAgeLimitLabel.setText(_translate("MainWindow", "0"))

    def asignCategory(self):
        if self.maleRadioButton.isChecked():
            category = Category(
                self.categoryNameLineEdit.text(),
                int(self.lowerAgeLimitLabel.text()),
                int(self.upperAgeLimitLabel.text()),
                "Male",
            )
            categoryList.append(category)
            for category in categoryList:
                pass

            popupmessage("Category has been saved successfully")
            self.categoryNameLineEdit.clear()
            self.horizontalSlider.setValue(0)
            self.horizontalSlider_2.setValue(0)

        else:
            category = Category(
                self.categoryNameLineEdit.text(),
                int(self.lowerAgeLimitLabel.text()),
                int(self.upperAgeLimitLabel.text()),
                "Female",
            )
            categoryList.append(category)

            popupmessage("Category has been saved successfully")
            self.categoryNameLineEdit.clear()
            self.horizontalSlider.setValue(0)
            self.horizontalSlider_2.setValue(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
