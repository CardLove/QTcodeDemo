#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "clsmythread.h"
#include "dialog.h"
#include "mythread.h"


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

    void slot_recivefirst();
    void slot_recivesecond();
    void slot_recivethird();

signals:
    void  sig_firt();
    void  sig_second();
    void  sig_third();


private slots:
    void on_pushButton_4_clicked();

    void on_pushButton_5_clicked();

private:
    Ui::MainWindow *ui;
    Dialog *dialogP;
    QThread thread1 ;
    QThread thread2 ;
    QThread thread3 ;
    clsMyThread * clsMyThreadP1;
    clsMyThread * clsMyThreadP2;
    clsMyThread * clsMyThreadP3;


};

#endif // MAINWINDOW_H

