#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}
// 第一个按钮 槽函数

void MainWindow::on_pushButton_clicked()
{
    ui->pushButton->setStyleSheet(tr("border-image: url(:/images/inquiry/程序查询/speakon.png);background-color:transparent;color: transparent;"));
}
// 第二个按钮槽函数
void MainWindow::on_pushButton_2_clicked()
{
    ui->pushButton->setStyleSheet(tr("border-image: url(:/images/inquiry/程序查询/speakon.png);background-color:transparent;color: transparent;"));
}
