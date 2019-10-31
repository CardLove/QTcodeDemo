#ifndef CLSMYTHREAD_H
#define CLSMYTHREAD_H

#include <QObject>
#include <QDebug>
#include <QThread>


class clsMyThread : public QObject
{
      Q_OBJECT
public:
    clsMyThread();
    ~clsMyThread();


public slots:
    void first();
    void second();
    void three();

signals:
    void sig_sendfirst();
    void sig_sendsecond();
    void sig_sendThird();
};

#endif // CLSMYTHREAD_H
