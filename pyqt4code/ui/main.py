# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys

from ui.mainwindow import MainWindowFoution
from ui.button.button import  ButtonFoution
from  ui.itemWidget.widget import  WidgetFoution
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindowFoution()
    # mainWindow.show()

    buttonObject = ButtonFoution()
    # buttonObject.show()

    widgetObject  = WidgetFoution()
    widgetObject.show()
    print "hello world! 世界 你好！"
    sys.exit(app.exec_())
