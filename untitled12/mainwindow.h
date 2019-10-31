#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "clsmythread.h"


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

public slots:
    void slot_myfirst();
    void slot_mysecond();
    void slot_mythird();

    void slot_recivefirst();
    void slot_recivesecond();
    void slot_recivethird();

signals:
    void  sig_firt();
    void  sig_second();
    void  sig_third();


private:
    Ui::MainWindow *ui;
//    QThread thread1 ;
//    QThread thread2 ;
//    QThread thread3 ;
//    clsMyThread * clsMyThreadP1;
//    clsMyThread * clsMyThreadP2;
//    clsMyThread * clsMyThreadP3;
    clsMyThread * clsMyThreadP1;
    QThread thread1 ;

};

#endif // MAINWINDOW_H

