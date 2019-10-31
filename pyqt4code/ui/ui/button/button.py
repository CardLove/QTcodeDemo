# -*- coding: UTF-8 -*-
import sys
from PyQt4.QtCore import *#  pyqtSignal, QObject,QAbstractTableModel
from PyQt4.QtGui import *

from PyQt4 import QtGui
from PyQt4 import QtCore
from button_Ui import Ui_Dialog
class ButtonFoution(QDialog,Ui_Dialog):  #  主类函数

    def __init__(self,parent=None):
        super(ButtonFoution,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("pushButtonTest")
        self.resize(480,640)
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.connect(self.checkBox, QtCore.SIGNAL('stateChanged(int)'),self.checkBoxChangeTitle)
        self.radioButton.toggled.connect(lambda :self.radioButtonChange(self.radioButton))
        self.connect(self.toolButton, QtCore.SIGNAL('toggled(bool)'),self.toolButtonChange)

        self.toolButton.clicked.connect(self.toolButtonClicked)
        self.toolButton.setCheckable(True)
        self.toolButton.setText('start')

        self.commandLinkButton.setText("Python")
        self.commandLinkButton.setDescription("hello world")
        self.commandLinkButton.setIcon(QIcon("image/21.jpg"))
        self.commandLinkButton.clicked.connect(self.commandLinkButtonClicked)

        self.buttonBox.accepted.connect(self.buttonBoxAccept)
        self.buttonBox.rejected.connect(self.buttonBoxReject)

    # pushbutton 槽函数
    def pushButtonClicked(self):
        print("pushButtonClicked")
        self.label.setText("pushButtonClicked")

    #checkBox
    def checkBoxChangeTitle(self,state):
        print("checkBoxChangeTitle:",state)
        self.label.setText("checkBoxChangeTitle")
#
    def radioButtonChange(self,tatue): #  tatue  radiobutton 的名字
        print("radioButtonChange")
        if tatue.text() == 'RadioButton':
            if tatue.isChecked() == True:
                print(tatue.text() + "is selected")
            else:
                print(tatue.text() + "is deselected")

    '''
    工具按钮（QToolButton）区别于普通按钮（QPushButton）的一点是，工具按钮（QToolButton）可以带图标，他们两个有同一个父类（QAbstractButton）;
    工具按钮（QToolButton）有两部分组成：文本text 和 图标icon（建议用png格式的图片）
    '''
    # 没有响应 需要调试
    def toolButtonChange(self,value):
        print("toolButtonChange",value)

    def toolButtonClicked(self):
        if self.toolButton.isChecked():
            print("toolButtonClicked")


    def commandLinkButtonClicked(self):
        print("commandLinkButtonClicked")

    #  按钮盒子
    def  buttonBoxAccept(self):
        print "buttonBoxAccept"

    def buttonBoxReject(self):
        print "buttonBoxReject"