# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(935, 681)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(9, 186, 391, 171))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.widget_3 = QtGui.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(9, 352, 411, 221))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.listWidget = QtGui.QListWidget(self.widget_3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.widget = QtGui.QWidget(self.widget_3)
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(65, 255, 249);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_4.addWidget(self.widget)
        self.stackedWidget = QtGui.QStackedWidget(self.widget_3)
        self.stackedWidget.setStyleSheet(_fromUtf8("background-color: rgb(149, 107, 255);"))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 55, 195);"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(9, 607, 150, 20))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.fontDialogPB = QtGui.QPushButton(self.centralwidget)
        self.fontDialogPB.setGeometry(QtCore.QRect(172, 135, 75, 23))
        self.fontDialogPB.setObjectName(_fromUtf8("fontDialogPB"))
        self.fileDialogPB = QtGui.QPushButton(self.centralwidget)
        self.fileDialogPB.setGeometry(QtCore.QRect(253, 135, 75, 23))
        self.fileDialogPB.setObjectName(_fromUtf8("fileDialogPB"))
        self.colorDialogPB = QtGui.QPushButton(self.centralwidget)
        self.colorDialogPB.setGeometry(QtCore.QRect(91, 135, 75, 23))
        self.colorDialogPB.setObjectName(_fromUtf8("colorDialogPB"))
        self.inputDialogPB = QtGui.QPushButton(self.centralwidget)
        self.inputDialogPB.setGeometry(QtCore.QRect(10, 135, 75, 23))
        self.inputDialogPB.setObjectName(_fromUtf8("inputDialogPB"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(156, 10, 54, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(83, 11, 73, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 32, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 580, 33, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.radioButtonYes = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonYes.setGeometry(QtCore.QRect(185, 582, 41, 16))
        self.radioButtonYes.setObjectName(_fromUtf8("radioButtonYes"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(43, 582, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(114, 582, 71, 16))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.radioButtonNo = QtGui.QRadioButton(self.centralwidget)
        self.radioButtonNo.setGeometry(QtCore.QRect(226, 582, 35, 16))
        self.radioButtonNo.setObjectName(_fromUtf8("radioButtonNo"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(261, 580, 87, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.comboBox_label = QtGui.QLabel(self.centralwidget)
        self.comboBox_label.setGeometry(QtCore.QRect(472, 580, 54, 16))
        self.comboBox_label.setObjectName(_fromUtf8("comboBox_label"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekSlider.setGeometry(QtCore.QRect(437, 580, 17, 20))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "新建项目", None))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "新建项目", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.fontDialogPB.setText(_translate("MainWindow", "字体对话框", None))
        self.fileDialogPB.setText(_translate("MainWindow", "文件对话框", None))
        self.colorDialogPB.setText(_translate("MainWindow", "颜色对话框", None))
        self.inputDialogPB.setText(_translate("MainWindow", "输入对话框", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "1", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "2", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "3", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "4", None))
        self.radioButtonYes.setText(_translate("MainWindow", "yes", None))
        self.checkBox.setText(_translate("MainWindow", "checkBox", None))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox", None))
        self.radioButtonNo.setText(_translate("MainWindow", "no", None))
        self.comboBox_label.setText(_translate("MainWindow", "TextLabel", None))

from PyQt4 import phonon