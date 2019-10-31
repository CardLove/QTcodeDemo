# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(530, 384)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 20, 411, 301))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.toolButton = QtGui.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(140, 50, 37, 18))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.radioButton = QtGui.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(210, 60, 89, 16))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.checkBox = QtGui.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(40, 120, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.frame)
        self.commandLinkButton.setGeometry(QtCore.QRect(170, 90, 188, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(30, 190, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 250, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.radioButton.setText(_translate("Dialog", "RadioButton", None))
        self.checkBox.setText(_translate("Dialog", "CheckBox", None))
        self.commandLinkButton.setText(_translate("Dialog", "CommandLinkButton", None))
        self.label.setText(_translate("Dialog", "TextLabel", None))

