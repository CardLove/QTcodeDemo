#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/23 23:57
# @Author : wang huixi
# @File   : update.py
from PyQt4.QtCore import  QAbstractTableModel#  pyqtSignal, QObject,QAbstractTableModel
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import QDialog
from  tableView_Ui import Ui_Dialog

from PyQt4.QtGui import QDesktopWidget
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QHeaderView
from PyQt4.QtSql import QSqlQueryModel
from PyQt4.QtSql import QSqlQuery
from PyQt4.QtSql import QSqlDatabase
from PyQt4.QtGui import QAbstractItemView
from PyQt4.QtCore import QDateTime
import operator


class tableView(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(tableView, self).__init__(parent)
        self.setupUi(self)
        self.sortFlag = 0
        self.log_db = None
        self.query_audit = 'AuthenticationAudit'
        self.log_model = QSqlQueryModel()
        self.init_data_db()
        """
        tableView
        """
        sql_str = ""

        self.log_model.setQuery(
            'select * from  {} {} order by OpenTime limit 30  '.format(self.query_audit, sql_str), self.log_db)
        print("  select * from  {} {} order by OpenTime limit 30  ".format(self.query_audit, sql_str))
        print self.log_model
        for row in range(4):
            for column in range(4):
                item = QStandardItem('row %s,column %s' % (row, column))
                # 设置每个位置的文本值
                self.log_model.setItem(row, column, item)
        self.set_table_model()
        self.tableView.setModel(self.log_model)
        self.set_table_view()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)


        self.pushButton.clicked.connect(self.onPushButtonClicked)
        self.pushButton_2.clicked.connect(self.onPushButtonClicked2)

        self.tableView.verticalHeader().sectionClicked.connect(self.VerSectionClicked)  # 表头单击信号
        self.tableView.horizontalHeader().sectionClicked.connect(self.HorSectionClicked)  # 表头单击信号

    def set_table_model(self):
        self.log_model.setHeaderData(0, Qt.Horizontal, "序号")
        self.log_model.setHeaderData(1, Qt.Horizontal, "用户账户")
        self.log_model.setHeaderData(2, Qt.Horizontal, "主机名称")
        self.log_model.setHeaderData(3, Qt.Horizontal, "事件时间")
        self.log_model.setHeaderData(4, Qt.Horizontal, "事件动作")

    def set_table_view(self):
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setColumnHidden(0, True)
        self.tableView.setColumnHidden(10, True)
        self.tableView.setSortingEnabled(True)#  自动排序

    def init_data_db(self):

        if QSqlDatabase.contains('zjsj_single_db'):
            self.log_db = QSqlDatabase.database('zjsj_single_db')
        else:
            self.log_db = QSqlDatabase.addDatabase('QSQLITE', 'zjsj_single_db')
        self.log_db.setDatabaseName("zjsj_single.db")

        if self.log_db.open():
            qry = QSqlQuery(self.log_db)
            qry.prepare('pragma journal_mode=wal;')
            cmd = "CREATE TABLE IF NOT EXISTS [{table_name}] (\
                        [ID] INTEGER PRIMARY KEY autoincrement NOT NULL,\
                        [UserName]  TEXT,\
                        [LocalHost]  TEXT,\
                        [OpenTime] TEXT,\
                        [EventAction] TEXT,\
                        [EventObject] TEXT,\
                        [EventHandling] TEXT,\
                        [EventDescription] TEXT,\
                        [Event_outcomes] TEXT,\
                        [LogLevel] TEXT,\
                        [LogXml] TEXT)"


            if not qry.exec_():
                print "sdfdsf"

    def VerSectionClicked(self, index):
        print index

    def HorSectionClicked(self, index):
        print "dsdsds"
        if  self.sortFlag:
            self.tableView.sortByColumn(1, 1)
            self.sortFlag = 0
        else:
            self.tableView.sortByColumn(1, 0)
            self.sortFlag = 1

    def onPushButtonClicked(self):
        print "dds"
        self.tableView.sortByColumn(1,1)

    def onPushButtonClicked2(self):
        print "dds2"
        self.tableView.sortByColumn(1,0)

