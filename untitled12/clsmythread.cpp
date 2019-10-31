#include "clsmythread.h"
#include <QThread>

clsMyThread::clsMyThread()
{
    qDebug() << "clsMyThread::clsMyThread()()"<<QThread::currentThreadId() <<endl;

}

clsMyThread::~clsMyThread()
{
    qDebug() << "clsMyThread::~clsMyThread()"<<  QThread::currentThreadId() <<endl;

}
void clsMyThread::first()
{
    qDebug() <<"111 clsMyThread first"<< QThread::currentThreadId();
    emit sig_sendfirst();


}

void clsMyThread::second()
{
    qDebug() << "222clsMyThread second" << QThread::currentThreadId();
    emit sig_sendsecond();

}

void clsMyThread::three()
{
    qDebug() << "333clsMyThread three" << QThread::currentThreadId();
    emit sig_sendThird();
}

