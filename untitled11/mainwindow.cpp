#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    qDebug() << "main" << QThread::currentThreadId();

    clsMyThreadP1 = new clsMyThread;
    clsMyThreadP1->moveToThread(&thread1);
    clsMyThreadP2 = new clsMyThread;
    clsMyThreadP2->moveToThread(&thread2);
    clsMyThreadP3 = new clsMyThread;
    clsMyThreadP3->moveToThread(&thread3);
    thread1.start();
    thread2.start();
    thread3.start();
    connect(&thread1, SIGNAL(finished()), this, SLOT(deleteLater()));
    connect(&thread2, SIGNAL(finished()), this, SLOT(deleteLater()));
    connect(&thread3, SIGNAL(finished()), this, SLOT(deleteLater()));

    connect(ui->pushButton, SIGNAL(clicked()), clsMyThreadP1, SLOT(first()), Qt::QueuedConnection);
    connect(ui->pushButton_2, SIGNAL(clicked()), clsMyThreadP2, SLOT(second()), Qt::QueuedConnection);
    connect(ui->pushButton_3, SIGNAL(clicked()), clsMyThreadP3, SLOT(three()), Qt::QueuedConnection);

    dialogP = new Dialog();
    dialogP->setWindowFlags(Qt::FramelessWindowHint|Qt::WindowStaysOnTopHint);
    dialogP->setWindowOpacity(0.9);//半透明
//    dialogP->show();






}

MainWindow::~MainWindow()
{
    qDebug() <<"MainWindow::~MainWindow()" << endl;
    if (&thread1)
    {
        if (thread1.isRunning())
        {
            qDebug() << "thread->isRunning()"<< thread1.isRunning()<< endl;
            thread1.quit();
            thread1.wait();
            thread2.quit();
            thread2.wait();
            thread3.quit();
            thread3.wait();
        }

    }
    if (clsMyThreadP1)
    {
        qDebug() << "clsMyThreadP1"<< clsMyThreadP1<< endl;
        delete clsMyThreadP1;
        clsMyThreadP1 = NULL;
    }
    if (clsMyThreadP2)
    {
        qDebug() << "clsMyThreadP2"<< clsMyThreadP2<< endl;
        delete clsMyThreadP2;
        clsMyThreadP2 = NULL;
    }
    if (clsMyThreadP3)
    {
        qDebug() << "clsMyThreadP3"<< clsMyThreadP3<< endl;
        delete clsMyThreadP3;
        clsMyThreadP3 = NULL;
    }

    delete ui;
}


void MainWindow::slot_recivefirst()
{
    qDebug() << "slot_recivefirst" << QThread::currentThreadId();
}

void MainWindow::slot_recivesecond()
{
    qDebug() << "slot_recivesecond" << QThread::currentThreadId();
}

void MainWindow::slot_recivethird()
{
    qDebug() << "slot_recivethird" << QThread::currentThreadId();
}



void MainWindow::on_pushButton_4_clicked()
{
//    dialogP->show();
//    dialogP->setLabelText("show");
}

void MainWindow::on_pushButton_5_clicked()
{
//    dialogP->hide();
//    dialogP->setLabelText("hide");
    myThread * myThreadP = new myThread();
    myThreadP->start();
}
