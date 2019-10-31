#!/usr/bin/python
# -*- coding: UTF-8 -*-

from checkBox_Ui import Ui_Dialog

from PyQt4.QtGui import QRadioButton
from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QStandardItemModel
from PyQt4.QtGui import QStandardItem
from PyQt4.QtGui import QAbstractItemView
from PyQt4.QtGui import QHeaderView

import sys
import  time
from datetime import datetime
from PyQt4.QtCore import QDateTime



class MyForm(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)

        self.ui = Ui_Dialog()
        self.checkBox1.stateChanged.connect(self.change_conditional_qurey_checkBox)
        self.pushButton.clicked.connect(self.data_sort)
        self.pushButton_2.clicked.connect(self.data_sort_2)
        self.radioButton.toggled.connect(self.radioButtonChange)

        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(['1', '2', '3', '4'])
        self.tableView.setSortingEnabled(True)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setColumnHidden(0, True)
        self.tableView.setColumnHidden(10, True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)

        connect(tableView, SIGNAL(clicked(const
        QModelIndex &)), this, SLOT(onTableClicked(const
        QModelIndex &)));

        for row in range(4):
            for column in range(4):
                item = QStandardItem('row %s,column %s' % (row, column))
                self.model.setItem(row, column, item)
        self.tableView.setModel(self.model)

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        time = time.split(".")[0]
        print(time)


        # self.dateTimeEdit.setDateTime(QDate.currentDate())
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        print(type(str(self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss").toUtf8())))
        print(str(self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss").toUtf8()))

    def data_sort(self):
        print 'jjjjjjjjjjjjjjjjjjjjjj'
        self.tableView.sortByColumn(1,Qt.DescendingOrder)

    def data_sort_2(self):
        print 'jjjjjjjjjjjjjjjjjjjjjj'
        self.tableView.sortByColumn(1,Qt.AscendingOrder)

    def radioButtonChange(self):
        print("dsd")
        if self.radioButton.text() == 'RadioButton':
            if self.radioButton.isChecked() == True:
                print(self.radioButton.text() + "is selected")
            else:
                print(self.radioButton.text() + "is deselected")



    def change_conditional_qurey_checkBox(self):

        if self.checkBox1.checkState() ==Qt.Checked:
            print("yes")
        else:
            print("sfsf")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
