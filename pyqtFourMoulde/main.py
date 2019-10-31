#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2019/11/23 23:57
# @Author : wang huixi
# @File   : update.py

from PyQt4 import QtGui
import sys

from  ui.mainwindow import MainWindowFoution

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindowFoution()
    mainWindow.show()
    print "hello world! 世界 你好！"
    sys.exit(app.exec_())