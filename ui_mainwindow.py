# Form implementation generated from reading ui file 'E:\MyProject\Python\RecognizeNumber\ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 552)
        MainWindow.setMinimumSize(QtCore.QSize(400, 552))
        MainWindow.setMaximumSize(QtCore.QSize(400, 552))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_0 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_0.setFont(font)
        self.label_0.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_0.setObjectName("label_0")
        self.horizontalLayout_2.addWidget(self.label_0)
        self.label_1 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_2.addWidget(self.label_1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar_0 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_0.sizePolicy().hasHeightForWidth())
        self.progressBar_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progressBar_0.setFont(font)
        self.progressBar_0.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_0.setProperty("value", 19)
        self.progressBar_0.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.progressBar_0.setTextVisible(False)
        self.progressBar_0.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_0.setObjectName("progressBar_0")
        self.horizontalLayout.addWidget(self.progressBar_0)
        self.progressBar_1 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_1.sizePolicy().hasHeightForWidth())
        self.progressBar_1.setSizePolicy(sizePolicy)
        self.progressBar_1.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_1.setProperty("value", 1)
        self.progressBar_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_1.setTextVisible(False)
        self.progressBar_1.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_1.setObjectName("progressBar_1")
        self.horizontalLayout.addWidget(self.progressBar_1)
        self.progressBar_2 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_2.setProperty("value", 1)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout.addWidget(self.progressBar_2)
        self.progressBar_3 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy)
        self.progressBar_3.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_3.setProperty("value", 1)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout.addWidget(self.progressBar_3)
        self.progressBar_4 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_4.sizePolicy().hasHeightForWidth())
        self.progressBar_4.setSizePolicy(sizePolicy)
        self.progressBar_4.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_4.setProperty("value", 1)
        self.progressBar_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_4.setObjectName("progressBar_4")
        self.horizontalLayout.addWidget(self.progressBar_4)
        self.progressBar_5 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_5.sizePolicy().hasHeightForWidth())
        self.progressBar_5.setSizePolicy(sizePolicy)
        self.progressBar_5.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_5.setProperty("value", 1)
        self.progressBar_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_5.setObjectName("progressBar_5")
        self.horizontalLayout.addWidget(self.progressBar_5)
        self.progressBar_6 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_6.sizePolicy().hasHeightForWidth())
        self.progressBar_6.setSizePolicy(sizePolicy)
        self.progressBar_6.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_6.setProperty("value", 1)
        self.progressBar_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_6.setObjectName("progressBar_6")
        self.horizontalLayout.addWidget(self.progressBar_6)
        self.progressBar_7 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_7.sizePolicy().hasHeightForWidth())
        self.progressBar_7.setSizePolicy(sizePolicy)
        self.progressBar_7.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_7.setProperty("value", 1)
        self.progressBar_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_7.setObjectName("progressBar_7")
        self.horizontalLayout.addWidget(self.progressBar_7)
        self.progressBar_8 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_8.sizePolicy().hasHeightForWidth())
        self.progressBar_8.setSizePolicy(sizePolicy)
        self.progressBar_8.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_8.setProperty("value", 1)
        self.progressBar_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_8.setTextVisible(False)
        self.progressBar_8.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_8.setObjectName("progressBar_8")
        self.horizontalLayout.addWidget(self.progressBar_8)
        self.progressBar_9 = QtWidgets.QProgressBar(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_9.sizePolicy().hasHeightForWidth())
        self.progressBar_9.setSizePolicy(sizePolicy)
        self.progressBar_9.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.progressBar_9.setProperty("value", 1)
        self.progressBar_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar_9.setTextVisible(False)
        self.progressBar_9.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.progressBar_9.setObjectName("progressBar_9")
        self.horizontalLayout.addWidget(self.progressBar_9)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setStyleSheet("border: 1px solid black; border-radius: 5px;")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 100)
        self.gridLayout.setRowStretch(2, 250)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_0.setText(_translate("MainWindow", "0"))
        self.label_1.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_6.setText(_translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "7"))
        self.label_8.setText(_translate("MainWindow", "8"))
        self.label_9.setText(_translate("MainWindow", "9"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
