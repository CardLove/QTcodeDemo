#ifndef MYTHREAD_H
#define MYTHREAD_H

#include <QObject>
#include <QThread>
#include <windows.h>
#include <QDebug>
class myThread : public QThread
{
    Q_OBJECT
public:
    myThread();
    void run();
};

#endif // MYTHREAD_H
