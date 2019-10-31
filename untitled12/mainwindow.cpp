#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    qDebug() << "main" << QThread::currentThreadId();

    clsMyThreadP1 = new clsMyThread;



    //用不同的法师调用mythread的方法
    connect(ui->pushButton, SIGNAL(clicked()), this, SLOT(slot_myfirst()), Qt::AutoConnection);








}

MainWindow::~MainWindow()
{
    qDebug() <<"MainWindow::~MainWindow()" << endl;
//    if (&thread1)
//    {
//        if (thread1.isRunning())
//        {
//            qDebug() << "thread->isRunning()"<< thread1.isRunning()<< endl;
//            thread1.quit();
//            thread1.wait();

//        }

//    }
//    if (clsMyThreadP1)
//    {
//        qDebug() << "clsMyThreadP1"<< clsMyThreadP1<< endl;
//        delete clsMyThreadP1;
//        clsMyThreadP1 = NULL;
//    }
//    if (clsMyThreadP2)
//    {
//        qDebug() << "clsMyThreadP2"<< clsMyThreadP2<< endl;
//        delete clsMyThreadP2;
//        clsMyThreadP2 = NULL;
//    }
//    if (clsMyThreadP3)
//    {
//        qDebug() << "clsMyThreadP3"<< clsMyThreadP3<< endl;
//        delete clsMyThreadP3;
//        clsMyThreadP3 = NULL;
//    }

    delete ui;
}


void MainWindow::slot_myfirst()
{
    qDebug() << "slot_myfirst" << QThread::currentThreadId();


    clsMyThreadP1->moveToThread(&thread1);
    thread1.start();
    connect(this, SIGNAL(sig_firt()), clsMyThreadP1, SLOT(first()), Qt::QueuedConnection);
    connect(clsMyThreadP1, SIGNAL(sig_sendfirst()), this, SLOT(slot_recivefirst()), Qt::QueuedConnection);
    connect(&thread1, SIGNAL(finished()), this, SLOT(deleteLater()));
    emit sig_firt();
}

void MainWindow::slot_mysecond()
{
    qDebug() << "slot_mysecond" << QThread::currentThreadId();

}

void MainWindow::slot_mythird()
{
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


