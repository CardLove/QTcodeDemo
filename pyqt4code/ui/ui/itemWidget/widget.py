# -*- coding: UTF-8 -*-
# -*- coding: UTF-8
import sys
from PyQt4.QtCore import *#  pyqtSignal, QObject,QAbstractTableModel
from PyQt4.QtGui import *

from PyQt4 import QtGui
from PyQt4 import QtCore
from widget_Ui import Ui_Dialog
class WidgetFoution(QDialog,Ui_Dialog):  #  主类函数

    def __init__(self,parent=None):
        super(WidgetFoution,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("WidgetTest")

        self.listWidget.resize(300, 120)
        self.listWidget.addItem("Item 1")
        self.listWidget.addItem("Item 2")
        self.listWidget.addItem("Item 3")
        self.listWidget.addItem("Item 4")


        self.treeWidget.setColumnCount(1)  # 设置部件的列数为2
        self.treeWidget.setHeaderLabels(['Key', 'Value'])  # 设置头部信息对应列的标识符

        # 设置root为self.tree的子树，故root是根节点
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, 'root')  # 设置根节点的名称

        # 为root节点设置子结点
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'name1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, 'name2')

        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0, 'child4')
        child4.setText(1, 'name4')

        self.treeWidget.addTopLevelItem(root)




