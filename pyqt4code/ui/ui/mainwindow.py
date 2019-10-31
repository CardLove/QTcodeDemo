# -*- coding: UTF-8 -*-
import sys
from PyQt4.QtCore import *#  pyqtSignal, QObject,QAbstractTableModel
from PyQt4.QtGui import *

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QDateTime

import operator

from mainwindow_Ui import Ui_MainWindow

class Communicate(QObject):

    closeApp = pyqtSignal()
#  table widget  model
class MyTableModel(QAbstractTableModel):
    """
    keep the method names
    they are an integral part of the model
    """

    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))


class MainWindowFoution(QMainWindow,Ui_MainWindow):  #  主类函数

    def __init__(self,parent=None):
        super(MainWindowFoution,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("pyqt4 learn")
        self.resize(480,640)
        self.setWindowIcon(QIcon('image/icon/icon.jpg'))

        exitAct = QAction(QIcon('image/icon/icon.jpg'), '&Exit', self)  #  行为
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar().showMessage('Ready')   # 状态栏

        menubar = self.menuBar()      # 菜单栏
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        # 次级的菜单栏
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)


        self.pushButton.setText("hello world! ")
        self.pushButton.clicked.connect(self.onPushButtonClicked)

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        """
        tableView
        """
        # you could process a CSV file to create this data
        header = ['First Name', 'Last Name', 'Age', 'Weight']
        # a list of (fname, lname, age, weight) tuples
        dataList = [
            ('Ben', 'Dover', 36, 127),
            ('Foster', 'Krampf', 27, 234),
            (u'对对对', 'Chaurus', 19, 315),
            ('Sede', 'Anowski', 59, 147),
            ('Carolus', 'Gabel', 94, 102),
            ('Michel', 'Zittus', 21, 175),
            ('Annie', 'Waters', 31, 114)
        ]

        table_model = MyTableModel(self, dataList, header)
        table_view = QTableView()
        # bind cell click to a method reference
        self.tableView.clicked.connect(self.showSelection)

        self.tableView.setModel(table_model)
        # enable sorting
        self.tableView.setSortingEnabled(True)



        # 创建列表窗口，添加条目
        self.listWidget.insertItem(0,u"联系方式")
        # self.listWidget.insertItem(1,'个人信息')
        # self.listWidget.insertItem(2,'教学程度')





        # # 在QStackedWidget对象中填充了三个子控件
        # self.stackedWidget = QStackedWidget(self)
        # self.stackedWidget.addWidget(self.widget)
        # self.stackedWidget.addWidget(self.widget_2)

        self.listWidget.currentRowChanged.connect(self.display)
        # # 垂直布局
        # layout = QGridLayout(self)
        #
        # # 控件添加到布局中，设置布局
        # layout.addWidget(self.widget,0,0)
        # layout.addWidget(self.widget_2,0,0)
        # self.widget_3.setLayout(layout)

        # comboBox
        #实例化QComBox对象
        # self.comboBox=QComboBox(self)
        # 单个添加条目
        self.comboBox.addItem('C')
        self.comboBox.addItem('C++')
        self.comboBox.addItem('Python')
        # 多个添加条目
        self.comboBox.addItems(['Java', 'C#', 'PHP'])
        # 当下拉索引发生改变时发射信号触发绑定的事件
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

        '''
        输入对话框
        '''
        self.inputDialogPB.clicked.connect(self.onFileDialogSlots)

        '''颜色对话框'''
        # self.connect(self.colorDialogPB, QtCore.SIGNAL('clicked()'),self.showColorDialog)
        self.colorDialogPB.clicked.connect(self.showColorDialog)
        # self.setFocus()

        '''字体对话框'''
        self.connect(self.fontDialogPB, QtCore.SIGNAL('clicked()'), self.showFontDialog)
        '''文件对话框'''
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        self.connect(self.fileDialogPB, QtCore.SIGNAL('clicked()'), self.showFileDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        #  checkBox
        self.checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.checkBox.toggle()
        self.connect(self.checkBox, QtCore.SIGNAL('stateChanged(int)'),
                     self.changeTitle)

        # 定时器
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.timer.start(100,self)















    def display(self, i):
        # 设置当前可见的选项卡的索引
        print "self.stackedWidget.setCurrentIndex(i)",i
        self.stackedWidget.setCurrentIndex(i)

    def selectionchange(self, i):
        # 标签用来显示选中的文本
        # currentText()：返回选中选项的文本
        self.comboBox_label.setText(self.comboBox.currentText())
        print('Items in the list are:')
        # 输出选项集合中每个选项的索引与对应的内容
        # count()：返回选项集合中的数目
        for count in range(self.comboBox.count()):
            print('Item' + str(count) + '=' + self.comboBox.itemText(count))
            print('current index', i, 'selection changed', self.comboBox.currentText())



        '''颜色对话框'''
    def showColorDialog(self):

        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.widget.setStyleSheet("QWidget { background-color: %s }"
                                      % col.name())
        '''
        输入对话框
        '''
    def onFileDialogSlots(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                     'Enter your name:')

        if ok:
            self.label.setText(str(text))
        else:
            self.label.setText("cannel")

    '''字体对话框'''
    def showFontDialog(self):

        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

    #  文件对话框
    def showFileDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                     '/home')
        fname = open(filename)
        data = fname.read()
        self.textEdit.setText(data)

    def onPushButtonClicked(self):
        self.label.setText(self.lineEdit.text())

    def keyPressEvent(self, e):
        print "重写系统键盘事件"
        # if e.key() == Qt.Key_Escape:
        #     self.close()
        # self.c.closeApp.emit()

    def showSelection(self, item):
        cellContent = item.data()
        print(cellContent)  # test
        sf = "You clicked on {}".format(cellContent)
        # display in title bar for convenience
        self.setWindowTitle(sf)

    #  checkBox
    def changeTitle(self, value):
        print  "changeTitle :  ",value
        if self.checkBox.isChecked():
            self.setWindowTitle('Checkbox')
            self.label.setText("Checkbox")
        else:
            self.setWindowTitle('')
            self.label.setText("")

        if value == Qt.Checked:
            print " yes "
            self.dateTimeEdit.setDisabled(True)
        else:
            print "no "
            self.dateTimeEdit.setDisabled(False)



# 定时器槽函数
    def timerEvent(self, event):
        # print "定时器槽函数",self.step

        self.step = self.step + 1
        if self.step <= 100:
            self.progressBar.setValue(self.step)
            self.label.setText(str(self.step))
        else:
            # label 显示图片
            pixmap = QtGui.QPixmap("image/icon/icon.jpg")
            self.label.setPixmap(pixmap)
            self.timer.stop()

