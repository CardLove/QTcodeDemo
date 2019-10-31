#include "mythread.h"

myThread::myThread()
{

}
void myThread::run()
{
    while(1)
    {
        sleep(1);
        qDebug() << "122121" << QThread::currentThreadId()  << endl;
    }
}
